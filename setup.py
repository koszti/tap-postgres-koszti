#!/usr/bin/env python

from setuptools import setup

setup(name='tap-postgres-koszti',
      version='1.0.3',
      description='Singer.io tap for extracting data from PostgreSQL',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      install_requires=[
          'singer-python==5.2.0',
          'requests==2.12.4',
	  'psycopg2==2.7.4',
	  'strict-rfc3339==0.7',
	  'nose==1.3.7'
      ],
      entry_points='''
          [console_scripts]
          tap-postgres=tap_postgres:main
      ''',
      packages=['tap_postgres', 'tap_postgres.sync_strategies']
)
