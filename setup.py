from setuptools import setup, find_packages

setup(
    name="easymenu3",
    version="0.3.0",
    author="PitterPatter",
    author_email="pitter@pitterpatter.io",
    description="A simple and customizable menu system for CLI applications.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pitterpatter22/EasyMenu3",
    packages=find_packages(),
    install_requires=[
        "pyfiglet",
        "icecream"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)