from setuptools import setup, find_packages

setup(
    name="shiori",
    version="0.1.0",
    packages=find_packages(where="."),  # プロジェクトルートの位置を指定
    package_dir={"": "."},                   # setup.py と同じ階層がルート
    python_requires=">=3.8",
)
