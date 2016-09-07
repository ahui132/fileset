from setuptools import setup, find_packages
setup(
    name = "fileset",
    version = "0.0.3",
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    scripts = ['fileset'],

    install_requires = [
        ],

    # metadata for upload to PyPI
    author = "hilojack",
    author_email = "a132811@gmail.com",
    description = "This is a cli tool used to calculate line set of two files",
    license = "GPL",
    keywords = "fileset",
    url = "http://github.com/hilojack/fileset", 

    # could also include long_description, download_url, classifiers, etc.
)
