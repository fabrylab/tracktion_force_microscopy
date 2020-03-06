#!/usr/bin/env python

from setuptools import setup
import os

version='1.2' # adding a version file automatically
file_path=os.path.join(os.getcwd(),os.path.join("pyTFM","_version.py"))
with open(file_path,"w") as f:
	f.write("__version__ = '%s'"%version)

setup(
    name='pyTFM',
    packages=['pyTFM'],
    version=version,
    description='traction force microscopy and FEM analysis of cell sheets',
    url='https://pytfm.readthedocs.io/',
    download_url = 'https://github.com/fabrylab/pyTFM.git',
    author='Andreas Bauer',
    author_email='andreas.b.bauer@fau.de',
    license='',
    install_requires=['numpy' ,'cython','openpiv==0.20.8; platform_system!="Windows"'
		      'openpiv_0.20.8_local; platform_system=="Windows"',
		      ,'scipy', 'scikit-image', 'matplotlib >= 2.1.2', 'tqdm', 'solidspy','clickpoints >= 1.9.0'], #[clickpoints 18.3] could be rather problematic
    
    dependency_links=[os.path.join(os.getcwd(),"local_dependencies","openpiv_0.20.8_local.whl"]
    keywords = ['traction force microscopy','finite elements'],
    classifiers = [],
    include_package_data=True,
    )


	
