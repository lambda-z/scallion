from __future__ import annotations

import os
from pydantic import BaseModel


class Settings(BaseModel):
    base_url: str = os.getenv("OPENAI_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY", 'sk-23186f4963ab487199ac2eb22b4c65a5')
    openai_model: str = os.getenv("OPENAI_MODEL", "qwen3-vl-plus")
    max_plan_revisions: int = int(os.getenv("MAX_PLAN_REVISIONS", "3"))


settings = Settings()
