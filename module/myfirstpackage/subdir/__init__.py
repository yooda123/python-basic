print("This is __init__.py in module2")

from .module2 import *
__all__ = ['myfunc', 'myfunc2']