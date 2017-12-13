"""
Lightweight Python Build Tool
"""

__version__ = "0.1.0"
__license__ = "MIT License"
__website__ = "http://oss.navio.tech/navio-builder/"
from ._nb import task, main
import pkgutil

__path__ = pkgutil.extend_path(__path__,__name__)

__all__ = ["task",  "main"]