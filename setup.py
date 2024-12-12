from setuptools import setup, find_packages

setup(
    name="SymMNA",
    version="0.1.0",
    description="A library for Symbolic Modified Nodal Analysis",
    author="Tiburonboy",
    packages=find_packages(),  # Automatically discover Python packages
    install_requires=[
        "numpy",  # Include any dependencies the library requires
    ],
    python_requires=">=3.7",
)
