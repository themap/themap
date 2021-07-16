import pathlib
from setuptools import find_packages,setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="themap",
    version="2.0.0",
    description="Python package to interact with themap APIs",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/themap/themap",
    author="Robert Mundinger",
    author_email="robert@themap.net",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    #packages=["map","layer","common","extras"],
    packages=find_packages(exclude=("tests","docs")),
    include_package_data=True,
    install_requires=["matplotlib"],
    entry_points={
        "console_scripts": [
            "hemap=themap.__main__:main",
        ]
    },
)