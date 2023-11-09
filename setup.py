from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


with open('requirements.txt') as f:
    requires = [l.strip() for l in f.readlines()]

setup(
    name="example",  
    version="0.0.1",  
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",  
    url="",  
    author="Isabel Cachola", 
    author_email="",  
    keywords="",  
    packages=find_packages(), 
    python_requires=">=3.7, <4",
    install_requires=requires
)