from setuptools import setup
import navio.meta_builder

setup(
    name="navio-builder-win",
    version=navio.meta_builder.__version__,

    author='Matthew Martin', # but also others, see github history
    author_email='matthewdeanmartin@gmail.com',
    url="https://github.com/matthewdeanmartin/navio-builder/tree/pypi_branch",

    packages=["navio", "navio.builder"],
    py_modules=["sh_it"],
    entry_points={'console_scripts': ['nb=navio.builder:main']},
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'sh'],
    install_requires=['sh'],
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
    description="navio-builder, but doesn't import sh and works on windows.",
    long_description="""See [navio-builder](https://pypi.org/project/navio-builder) for details. 
    This fork exists only to get windows compatibility.""",
    long_description_content_type='text/markdown'
)
