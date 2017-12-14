#!/usr/bin/python

import subprocess
from navio.builder import task

@task()
def apidoc():
    """
    Generate API documentation using epydoc.
    """
    subprocess.call(["epydoc","--config","epydoc.config"])
    
@task()
def test(*args):
    """
    Run unit tests.
    """
    subprocess.call(["py.test-2.7"] + list(args))
    subprocess.call(["py.test-3.3"] + list(args))

@task()
def check_uncommited():
    result = subprocess.check_output(['git', 'status', '--porcelain'])
    if result:
      raise 'There are uncommited files'

@task()
def generate_rst():
    
    subprocess.call(['pandoc', '-f', 'markdown', '-t', 'rst', '-o', 'README.rst', 'README.md'])
    subprocess.call(['pandoc', '-f', 'markdown', '-t', 'rst', '-o', 'CHANGES.rst', 'CHANGES.md'])


@task(generate_rst)
def upload():
    subprocess.call(['ssh-add', '~/.ssh/id_rsa'])
    subprocess.call(['python', 'setup.py', 'sdist', 'bdist_wininst', 'upload'])

@task(test, check_uncommited, generate_rst)
def release():
  pass

__DEFAULT__ = test