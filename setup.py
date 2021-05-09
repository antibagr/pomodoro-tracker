import pathlib
from setuptools import setup

BASE_DIR = pathlib.Path(__file__).parent

README = (BASE_DIR / "README.md").read_text()

setup(
    name="rudie-pomodoro-tracker",
    version="0.0.1",
    description="Pomodoro tracker with CLI interface.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/antibagr/pomodoro-tracker.git",
    author="Anton Bagryanov",
    author_email="rudiemeant@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["pomodoro_tracker"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pomodoro=pomodoro_tracker.__main__:run_tracker",
        ]
    },
)
