from setuptools import setup, find_packages

setup(
    name = 'lightshow',
    version = '0.1.0',
    url = 'http://predicate.us',
    author = 'Predicate Academy',
    author_email = 'mike@predicate.us',
    packages = ['lightshow'],
    install_requires = ['gpiozero'],
    include_package_data = True
)

