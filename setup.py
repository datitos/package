import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mendotimeseries",
    version="0.0.2",
    author="Mendo Team",
    author_email="pm@mendoteam.com",
    description="A time series prediction package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/datitos/package",
    packages=setuptools.find_packages(),
    install_requires=[
        'fbprophet>=0.7',
        'pandas>=0.23.3',
        'numpy>=1.14.5',
        'matplotlib>=2.2.0',
        'jupyter'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
