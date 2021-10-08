import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="imgdup",
    version="0.0.1",
    author="Pierre Hugo",
    description="Duplicate image detection as a service.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["imgdup"],
    package_dir={'':'.'},
    install_requires=['requests']
)
