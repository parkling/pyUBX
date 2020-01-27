from setuptools import setup


def readme():
    with open('readme.md') as f:
        return f.read()


setup(name='pyubx',
      version='0.0.1',
      description='A small but functional Python3 wrapper for the u-blox M8 UBX protocol, as defined in UBX-13003221 - R13, §31.',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3',
          'Topic :: Communications'
      ],
      url='https://github.com/mayeranalytics/pyUBX',
      author='Mayer Analytics',
      author_email='info@mayeranalytics.com',
      license='GNU GPL v3',
      packages=['pyubx'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
