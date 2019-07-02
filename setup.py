from distutils.core import setup

setup(
    name='lilies',
    version='0.0.2',
    description='A tool for creating colorful, formatted command line output',
    url='https://github.com/mrz1988/lilies',
    license='MIT',
    author='Matt Zychowski',
    author_email='mrz2004@gmail.com',
    packages=['lilies'],
    install_requires=[
        'colorama',
    ],
)
