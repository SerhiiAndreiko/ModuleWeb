from setuptools import setup, find_packages

setup(
    name='Bot Helper',
    version='0.1',
    description='bot',
    author='Serhii Andreiko',
    author_email='fantom784507@gmail.com',
    packages=find_packages(),
    install_requires=[
        
    ],
    entry_points={
        'console_scripts': ['bot = Book.bot:main'],
    }
)
