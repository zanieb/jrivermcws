from setuptools import setup

setup(name='jrivermcws',
      license='MIT',
      description=('Command-line interaction with the JRiver MCWS'),
      version='0.0.1',
      author='Michael Adkins',
      install_requires=['requests'],
      entry_points={'console_scripts': ['jriverctl = jrivermcws.__main__:main']},
    )
