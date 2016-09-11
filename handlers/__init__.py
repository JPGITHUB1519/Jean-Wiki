# __init__.py are used to mark directories on disk as Python package directories
# importing all modules from dir
from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f)]