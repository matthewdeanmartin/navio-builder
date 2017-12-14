"""
Lightweight Python Build Tool
"""

__version__ = "0.1.7"
__license__ = "MIT License"
__website__ = "https://oss.navio.tech/navio-builder/"
__download_url__ = 'https://github.com/naviotech/navio-builder/archive/{}.tar.gz'.format(__version__),
from ._nb import task, main
import pkgutil

__path__ = pkgutil.extend_path(__path__,__name__)

__all__ = ["task",  "main"]