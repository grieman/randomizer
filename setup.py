from distutils.core import setup
import py2exe
setup(
    console = ['picklunch.py'],
    options = {
        'py2exe': {
            'packages': ['googleplaces','numpy','csv']
        }
    })