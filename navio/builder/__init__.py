'''
Lightweight Python Build Tool
'''

from ._nb import task
from ._nb import add_env
from ._nb import main, nsh
from ._nb import dump, pushd, zipdir
try:
    import sh
except ModuleNotFoundError:
    import sh_it as sh

import pkgutil

__path__ = pkgutil.extend_path(__path__, __name__)

__all__ = [
    'task', 'main',
    'nsh', 'sh',
    'zipdir', 'add_env',
    'dump', 'dumps', 'pushd',
    'print_out', 'print_err'
]
