from setuptools import setup, find_packages

setup(
    name='tickers',
    version='0.1',
    packages=find_packages(),
    description='A package for getting market data',
    long_description=open('README.md').read(),
    author='Andrew Nelson',
    author_email='your-email@example.com',
    license='MIT',
    url='http://github.com/yourusername/tickers',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'yfinance',
        'pandas',
        'numpy',
    ],
)