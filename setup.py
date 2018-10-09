import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topo",
    version="0.0.1",
    author="Daniel Mesejo-Leon",
    author_email="mesejoleon@gmail.com",
    description="A simple topological sort implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mesejo/topo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)