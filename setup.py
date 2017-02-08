#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pkgutil import walk_packages
from setuptools import setup, find_packages


def read_file(filename):
    with open(filename) as fp:
        return fp.read().strip()


def read_rst(filename):
    # Ignore unsupported directives by pypi.
    return '\n'.join(line for line in read_file(filename).splitlines()
                     if not line.startswith('.. comment::'))


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


setup_attrs = dict(
    name='awesome-codename',
    version=read_file('VERSION'),
    description="Awesome Codename Generator",
    long_description=read_rst('README.rst') + '\n\n' + read_rst('HISTORY.rst'),
    author="Rolando (Max) Espinoza",
    author_email='rolando at rmax.io',
    url='https://github.com/rolando/awesome-codename',
    packages=list(find_packages('src')),
    package_dir={'': 'src'},
    package_data={'awesome_codename': ['data/*']},
    entry_points={'console_scripts': ['awesome-codename = awesome_codename.__main__:main']},
    install_requires=read_requirements('requirements/install.txt'),
    include_package_data=True,
    license="AGPL",
    keywords='awesome-codename',
    classifiers=[
        'Development Status :: 2 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)


if __name__ == "__main__":
    setup(**setup_attrs)
