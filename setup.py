from setuptools import setup, find_packages

setup(name='optimierung',
      version='0.1',
      description='lecture on optimization collection of methods',
      url='https://github.com/markus-abel/numericalOptimization',
      author='Studeten der Universitaet Potsdam',
      author_email='markus.abel@uni-potsdam.de',
      license='TBD',
      zip_safe=False,
      packages=find_packages(exclude=('tests',)),
      )
