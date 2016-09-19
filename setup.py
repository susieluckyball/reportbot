try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os import path

# README = path.abspath(path.join(path.dirname(__file__), 'README.rst'))

# This pkg is used to test conda build

setup(
      name='reportbot',
      version='0.0.1',
      description="Susie's awesome package example",
      author='Susie Zhang',
      author_email='susieluckyball@gmail.com',
      url='https://github.com/susieluckyball/reportbot',
      packages=['reportbot', "reportbot.monitor_tools"],
      entry_points={
        'console_scripts': [
          'report_run = reportbot.cli:report_run'
        ]
      },
      license='MIT'
)