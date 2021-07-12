import re
from pathlib import Path
from pytest_qasync import __version__, __author__, __author_email__, __description__

from setuptools import setup, find_packages


setup(
    name="pytest-qasync",
    version=__version__,
    packages=find_packages(),
    url="https://github.com/innodatalabs/pytest-qasync",
    license="MIT",
    author="Mike Kroutikov",
    author_email="mkroutikov@innodata.com",
    description="Pytest support for qasync.",
    long_description=Path(__file__).parent.joinpath("README.md").read_text(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Testing",
        "Framework :: Pytest",
    ],
    python_requires=">= 3.9",
    install_requires=["pytest >= 5.4.0"],
    extras_require={
        "testing": [
            "coverage",
            "hypothesis >= 5.7.1",
        ],
    },
    entry_points={"pytest11": ["qasync = pytest_qasync.plugin"]},
)
