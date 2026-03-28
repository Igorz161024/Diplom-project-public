from setuptools import setup, find_packages

setup(
    name="erp_diplom",
    version="0.1.0",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "erp_diplom=main:app",
        ],
    },
    python_requires=">=3.12",
    author="Ігор",
    description="ERP дипломний проєкт на FastAPI",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/твій_репозиторій",
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Framework :: FastAPI",
        "Operating System :: OS Independent",
    ],
)