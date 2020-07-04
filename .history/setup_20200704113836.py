from setuptools import setup
with open("README.MD","r") as fh:
    long = fh.read()
setup(
    name = 'RequestSoup',
    version='1.0.3',
    description='A wrapper created to make using requests and BeautifulSoup in conjunction easier',
    long_description=long,
    long_description_content_type="text/markdown",
    author="Arnav Chawla",
    author_email="arnavchawla23@gmail.com",
    # url = "https://github.com/ArnavChawla/RequestSoup",
    py_modules=["Python-Shopify"],
    package_dir={'':'src'},
    install_requires = [
        "RequestSoup"
    ],
    classifiers=[
    "License :: OSI Approved :: MIT License",
    ],
)