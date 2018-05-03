import io
import os
import re
from setuptools import setup, find_packages


def local_file(*name):
    return os.path.join(
        os.path.dirname(__file__),
        *name)


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def read_version():
    version_file = local_file('zaweb', 'version.py')
    local_vars = {}
    with open(version_file) as handle:
        exec(handle.read(), {}, local_vars)  # pylint: disable=exec-used
    return (local_vars['__version__'], local_vars['__version_info__'])



long_description = read('README.rst', mode='rt')

setup(
    name='zaweb',
    version=read_version()[0],
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),

    author='Sixty North AS',
    author_email='austin@sixty-north.com',
    description='A web front-end for Zorkalike',
    license='MIT',
    keywords='',
    url='https://github.com/sixty-north/introduction-to-python',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Education',
        'Topic :: Games/Entertainment :: Role-Playing',
    ],
    platforms='any',
    include_package_data=True,
    install_requires=[
        'aiohttp',
        'zorkalike'
    ],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax, for
    # example: $ pip install -e .[dev,test]
    extras_require={
        # 'dev': ['check-manifest', 'wheel'],
        # 'doc': ['sphinx', 'cartouche'],
        # 'test': ['hypothesis', 'pytest'],
    },
    entry_points={
        'console_scripts': [
           'zaweb = zaweb.app:main',
        ],
    },
    long_description=long_description,
)
