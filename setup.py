from setuptools import setup
import navio.builder
setup(
    name = "navio-builder",
    version =  navio.builder.__version__,
    author = "Peter Salnikov",
    author_email = "peter@navio.tech",
    url = navio.builder.__website__, 
    packages = ["navio", "navio.builder"],
    entry_points =  {'console_scripts': ['nb = navio.builder:main']}, 
    license = "MIT License",
    description = "Lightweight Python Build Tool.",
    long_description = open("README.md").read()+"\n"+open("CHANGES.md").read()
)
