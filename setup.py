from setuptools import setup

VERSION = '1.0.4'

setup(
  name = 'pyvesc',
  packages = ['pyvesc', 'pyvesc.packet', 'pyvesc.messages'],
  version = VERSION,
  description = 'Python implementation of the VESC communication protocol.',
  author = 'Liam Bindle',
  author_email = 'liambindle@gmail.com',
  url = 'https://github.com/LiamBindle/PyVESC',
  download_url = 'https://github.com/LiamBindle/PyVESC/tarball/' + VERSION,
  keywords = ['vesc', 'VESC', 'communication', 'protcol', 'packet'],
  classifiers = [],
  install_requires = ['PyCRC']
)
