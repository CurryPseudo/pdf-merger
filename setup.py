import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdf_merger",
    version="0.0.3",
    author="CurryPseudo",
    author_email="currypseudo@gmail.com",
    description="A script used for merge some pdf files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CurryPseudo/pdf-merger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
