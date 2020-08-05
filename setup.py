# -*- coding: utf-8 -*-
from setuptools import setup
from os import path

# Imports content of requirements.txt into setuptools' install_requires
try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except Exception:
    requirements = []


def get_version():
    with open('src/moresystemctlstatus/moresystemctlstatus.py') as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


# Imports content of README.md into setuptools' long_description
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='more-systemctl-status',
      version=get_version(),
      description='Provides children data of systemctl status processes. Wrapper for systemctl status and pstree.',
      long_description=long_description,
      keywords='systemd, pstree, process, wrapper, cli, sysadmin',
      author='Arturo "Buanzo" Busleiman',
      author_email='buanzo@buanzo.com.ar',
      url='https://github.com/buanzo/more-systemctl-status',
      license='Apache',
      zip_safe=False,
      python_requires='>=3.6',
      packages=['moresystemctlstatus'],
      package_dir={'moresystemctlstatus': 'src/moresystemctlstatus'},
      include_package_data=True,
      install_requires=requirements,
      entry_points={
         'console_scripts': [
            'more-systemctl-status = moresystemctlstatus.moresystemctlstatus:run',
         ],
      },
      classifiers=[
         'Environment :: Console',
         'Intended Audience :: Developers',
         'Intended Audience :: System Administrators',
         'License :: OSI Approved :: Apache Software License',
         'Natural Language :: English',
         'Operating System :: POSIX :: Linux',
         'Operating System :: POSIX :: Other',
         'Operating System :: POSIX',
         'Programming Language :: Python',
         'Programming Language :: Python :: 3 :: Only',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7',
         'Programming Language :: Python :: 3.8',
         'Programming Language :: Python :: Implementation :: PyPy', ],)
