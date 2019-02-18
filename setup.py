import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ReutersNews",
    version="1.1.0",
    author="Hurin Hu",
    author_email="hurin@live.ca",
    description="Search company's news on Reuters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HurinHu/ReutersNews",
    packages=setuptools.find_packages(),
    install_requires=['pandas'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
