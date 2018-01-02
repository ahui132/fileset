from setuptools import setup, find_packages
setup(
    name = "fileset",
    version = "0.0.4",
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    scripts = ['fileset'],

    install_requires = [],

    # metadata for upload to PyPI
    author = "ahui132",
    author_email = "a132811@gmail.com",
    description = "This is a cli tool used to calculate line set of two files",
    license = "GPL",
    keywords = "fileset",
    url = "http://github.com/ahui132/fileset", 

    # could also include long_description, download_url, classifiers, etc.
)
