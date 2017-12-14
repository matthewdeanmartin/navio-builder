from setuptools import setup
import navio.builder
setup(
    name="navio-builder",
    version=navio.builder.__version__,
    author="Peter Salnikov",
    author_email="peter@navio.tech",
    url=navio.builder.__website__,
    packages=["navio", "navio.builder"],
    entry_points={'console_scripts': ['nb=navio.builder:main']},
    license="MIT License",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Build Tools'
    ],
    keywords=['devops', 'build tool'],
    description="Lightweight Python Build Tool.",
    long_description=open("README.rst").read()+"\n"+open("CHANGES.rst").read()
)
