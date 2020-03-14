import setup tools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GOSH-FHIRworks-2020-FHIRByVoice", # Replace with your own username
    version="0.0.1",
    author="Sibghah Khan",
    author_email="sibghah.khan.18@ucl.ac.uk",
    description="Search and filter FHIR data using voice.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sibghah/GOSH-FHIRworks-2020-FHIRByVoice",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)