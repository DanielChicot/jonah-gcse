import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jona-gcse", # Replace with your own username
    version="0.0.1",
    author="Jonah McCarthy",
    author_email="jonah@gmail.com",
    description="Carpet quotation generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/micmac303/jonah-gcse",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)