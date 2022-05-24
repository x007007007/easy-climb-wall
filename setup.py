
# -*- coding: utf-8 -*-
from setuptools import setup

long_description = None
INSTALL_REQUIRES = [
    'django',
    'psutil',
    'docker',
    'gunicorn',
    'gevent',
    'setuptools<=57.4',
]

setup_kwargs = {
    'name': 'easy-climb-wall',
    'version': '0.1.0',
    'description': '',
    'long_description': long_description,
    'license': 'MIT',
    'author': '',
    'author_email': 'xingci.xu <x007007007@hotmail.com>',
    'maintainer': None,
    'maintainer_email': None,
    'url': '',
    'packages': [
        'x007007007.easyclimbwall',
        'x007007007.common',
        'x007007007.easyclimbwall.apps',
        'x007007007.easyclimbwall.apps.config',
        'x007007007.easyclimbwall.apps.config.migrations',
        'x007007007.easyclimbwall.apps.config.management',
        'x007007007.easyclimbwall.apps.config.management.commands',
        'x007007007.common.djapp',
        'x007007007.common.djapp.pipeline',
        'x007007007.common.djapp.pipeline.models',
    ],
    'package_dir': {'': 'src'},
    'package_data': {'': ['*']},
    'install_requires': INSTALL_REQUIRES,
    'python_requires': '>=3.10',

}


setup(**setup_kwargs)

