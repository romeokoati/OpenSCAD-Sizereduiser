#!/usr/bin/env python
"""
Setup configuration
"""

from setuptools import find_packages, setup
from osm.osm import __doc__ as module_doc

setup(
    name = 'OpenSCAD-Sizereduiser',
    version = '0.1',
    description = 'Reduce the size of your .scad file',
    long_description = module_doc,
    url = 'https://github.com/romeokoati/OpenSCAD-Sizereduiser',
    keywords = 'OpenSCAD SCAD CAD minimizer generator text code',
    packages = find_packages(exclude=['tests']),
    install_requires = [],
    entry_points = {
        'console_scripts': ['osm = osm.osm:main']},
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Topic :: Text Processing :: Filters',
        'Topic :: Utilities',
    ],
    test_suite = 'tests.tests',
    author = 'KOATI NEMALEU ROMEO',
    author_email = 'koatik@knracademie.com',
    maintainer = 'KOATI NEMALEU ROMEO',
    maintainer_email = 'romeokoatik@gmail.com',
    download_url = 'https://github.com/romeokoati/OpenSCAD-Sizereduiser',
    platforms = ['POSIX', 'Windows'],
    license = 'GPL v3 or newer',
    )
