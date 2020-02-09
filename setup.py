import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tofu", 
    version="0.0.1",
    author="Spiros Denaxas",
    author_email="s.denaxas@ucl.ac.uk",
    description="A Python library for generating synthetic UK Biobank data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spiros/tofu.gitt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
