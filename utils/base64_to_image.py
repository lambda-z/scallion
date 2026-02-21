import base64
import re
from pathlib import Path
from typing import Optional, Tuple

def base64_to_image(
    b64_str: str,
    out_path: str,
    force_ext: Optional[str] = None
) -> Tuple[str, str]:
    """
    将 base64 字符串保存为图片文件。

    参数:
        b64_str: base64 字符串（可带 data:image/png;base64, 前缀）
        out_path: 输出路径（例如 'out.png' 或 'out'）
        force_ext: 强制扩展名（例如 'png' / 'jpg'），传 None 则自动从 data URI 推断或使用 out_path 的后缀

    返回:
        (最终保存路径, mime类型/推断类型)
    """
    s = b64_str.strip()

    mime = "application/octet-stream"
    # 处理 data URI: data:image/png;base64,xxxx
    m = re.match(r"^data:(image\/[a-zA-Z0-9.+-]+);base64,(.*)$", s, re.DOTALL)
    if m:
        mime = m.group(1).lower()
        s = m.group(2).strip()

    # 某些 base64 会混入换行/空格
    s = re.sub(r"\s+", "", s)

    img_bytes = base64.b64decode(s, validate=False)

    p = Path(out_path)

    # 确定扩展名
    ext = None
    if force_ext:
        ext = force_ext.lower().lstrip(".")
    elif p.suffix:
        ext = p.suffix.lower().lstrip(".")
    else:
        # 尝试从 mime 推断
        if mime.startswith("image/"):
            ext = mime.split("/", 1)[1]
        else:
            ext = "png"  # 兜底

    # 没有后缀则补上
    if not p.suffix:
        p = p.with_suffix("." + ext)

    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(img_bytes)

    return str(p), mime


if __name__ == '__main__':
    # 1) 纯 base64
    save_path, mime = base64_to_image(b64_str, "output.jpg")
    print(save_path, mime)

    # 2) data URI
    save_path, mime = base64_to_image(data_uri_str, "output")  # 自动补后缀
    print(save_path, mime)

    # 3) 强制输出 png
    save_path, mime = base64_to_image(b64_str, "output_anyname", force_ext="png")
    print(save_path, mime)
