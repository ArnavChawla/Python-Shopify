from setuptools import setup
with open("README.MD","r") as fh:
    long = fh.read()
setup(
    name = 'shopi-py',
    version='1.0.1',
    description='An unnofical python package to interact with shopify stores',
    long_description=long,
    long_description_content_type="text/markdown",
    author="Arnav Chawla",
    author_email="arnavchawla23@gmail.com",
    # url = "https://github.com/ArnavChawla/RequestSoup",
    py_modules=["ShopiPy"],
    package_dir={'':'src'},
    install_requires = [
        "RequestSoup"
    ],
    classifiers=[
    "License :: OSI Approved :: MIT License",
    ],
)