import sys

extra = {}
if sys.version_info >= (3, 0):
    extra.update(use_2to3=True)

try:
    from setuptools import setup, find_packages, Command
except ImportError:
    from distutils.core import setup, find_packages, Command

author = "Marc Abramowitz"
email = "marc@marc-abramowitz.com"
version = "0.0.1-dev"
desc = """Download a package and run tox on it"""
long_desc = open('README.rst').read()

setup(name='piptox',
      version=version,
      description=desc,
      long_description=long_desc,
      data_files=[('', ['README.rst'])],
      classifiers=[
            'License :: OSI Approved :: BSD License',
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.4',
            'Programming Language :: Python :: 2.5',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.1',
          ],
      author=author,
      author_email=email,
      url='http://github.com/msabramo/anyserializer',
      license='BSD',
      py_modules=['piptox'],
      zip_safe=False,
      platforms=["any"],
      test_suite='tests',
      entry_points={'console_scripts': ['piptox = piptox:main']},
      **extra
)
