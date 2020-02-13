"""
molpy
Workshop package
"""

# Add imports here
from .molpy import *
from . import util 
from . import data

# Handle versioneer
from ._version import get_versions
diff --git /molpy/data/__init__.py /molpy/data/__init__.py

versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
