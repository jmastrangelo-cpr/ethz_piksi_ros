## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['piksi_pps_sync'],
    package_dir={'':'python'},
    scripts=['scripts/evaluate_pps']
    )

setup(**setup_args)
