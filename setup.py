__author__ = 'samsung'
from distutils.core import setup
import py2exe

setup(
    windows  = ['RandomMusic.py'],
    options = {
        "py2exe" : {
            "includes" : ["PySide.QtGui", "os", "random"]
        }
    }
)