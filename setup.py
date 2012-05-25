#setup script for TARDIS software

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from distutils.extension import Extension
from Cython.Distutils import build_ext

import glob
import numpy
#version number
version = '0.01dev'
#from distutils.core import setup


# Treat everything in scripts except README.rst as a script to be installed
scripts = glob.glob('scripts/*')
try:
	scripts.remove('scripts/README.rst')
except ValueError:
	pass


setup(name='tardis',
    description='TARDIS Software - Time And Relative Diffusion in Supernovae',
    author='The TARDIS collaboration',
    version=version,
    packages=['tardis'],
    package_data={'tardis': ['data/*']},
    scripts=scripts,
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("tardis/c_distance", ["tardis/cython-src/c_distance.pyx"]),
                   Extension("tardis.c_montecarlo", ["tardis/cython-src/c_montecarlo.pyx"], 
                        include_dirs=[numpy.get_include()],
                        libraries=['m'],
                        extra_compile_args=['-fopenmp'],
                        extra_link_args=['-fopenmp'])]    
    )
      