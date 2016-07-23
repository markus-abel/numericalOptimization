from setuptools import setup


def read(fname, as_list=False):
    """Read text file and return content as string."""
    import os
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        content = f.read()
    return content.split('\n') if as_list else content


setup(name='numOpt',
      version='0.2',
      description='Collection of Methods and Example Code for the Lecture on Optimization',
      url='https://github.com/markus-abel/numericalOptimization',
      author='Students of the University Potsdam',
      author_email='markus.abel@uni-potsdam.de, tino.goetzke@uni-potsdam.de',
      license='MIT',
      zip_safe=False,
      packages=['numopt'],
      python_requires='>=3.6',
      install_requires=read('requirements.txt', as_list=True),
      )
