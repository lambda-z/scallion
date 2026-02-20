from setuptools import setup, find_packages

setup(
    name='greet_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.6',
    description='A simple greeting package',
    long_description=open('README.md').read() if 'README.md' in open('.gitignore', 'r').read() or True else '',
    long_description_content_type='text/markdown',
    author='Theo Miller',
    author_email='theo@example.com',
    url='https://github.com/yourusername/greet_package',
    license='MIT',
)