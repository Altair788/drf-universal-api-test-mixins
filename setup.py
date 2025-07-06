from setuptools import setup, find_packages

setup(
    name="drf-universal-api-test-mixins",
    version="0.1.0",
    description="Универсальные миксины для тестирования DRF API",
    author="Eduard Slobodyanik",
    author_email="slobodyanik.ed@gmail.com",
    url="https://github.com/Altair788/drf-universal-api-test-mixins",
    packages=find_packages(),
    install_requires=[
        "Django>=3.2",
        "djangorestframework>=3.12"
    ],
    python_requires=">=3.8",
    license="MIT",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    project_urls={
        "Telegram": "https://t.me/eslobodyanik",
        "GitHub": "https://github.com/Altair788/drf-universal-api-test-mixins",
    },
)
