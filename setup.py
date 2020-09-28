import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mendotimeseries-MENDOTEAM",
    version="0.0.1",
    author="Mendo Team",
    author_email="pm@mendoteam.com",
    description="A time series prediction package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/datitos/package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
