import os
from setuptools import setup


DIRNAME = os.path.dirname(__file__)
ABSPATH = os.path.abspath(__file__)
README = open(os.path.join(DIRNAME, 'README.md')).read()

os.chdir(os.path.normpath(os.path.join(ABSPATH, os.pardir)))

setup(
    name='django-metadata',
    version='1.2',
    packages=['metadata'],
    include_package_data=True,
    license='Free Use',
    description='''This is a simple addon to your models, with this package you
can add metadata to any of your models''',
    long_description=README,
    url='https://github.com/calazans10/django-metadata',
    author='Jeferson Farias Calazans',
    author_email='calazans10@gmail.com',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Environment :: Plugins",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: Freeware",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
    ],
)
