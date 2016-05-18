from distutils.core import setup
from setuptools import find_packages
import dripemail

setup(
    name=dripemail.__app_name__,
    packages=find_packages(exclude=('tests',)),
    version=dripemail.__version__,
    author='Madra David',
    author_email='david@madradavid.com',
    url=dripemail.__app_url__,
    download_url='https://github.com/madra/dripemail/tarball/0.1',
    description='Drip email for Django',
    license='MIT',
    long_description=open('README.rst').read(),
    install_requires=['Django>=1.4'],
    keywords=['drip email', 'lead generation'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)
