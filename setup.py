from setuptools import setup
import navio.meta_builder

setup(
    name="navio-builder",
    version=navio.meta_builder.__version__,
    author='Navio Online OpenSource projects',
    author_email='oss@navio.online',
    url=navio.meta_builder.__website__,
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
    description="Lightweight Python Build Tool",
    long_description="{}\n{}".format(
        open("README.md", 'rb').read().decode('utf-8'),
        open("CHANGES.md", 'rb').read().decode('utf-8')
    ),
    long_description_content_type='text/markdown'
)
