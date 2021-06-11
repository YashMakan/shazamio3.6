
from setuptools import setup, find_packages

setup(
    name='shazamyash',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['aiofiles','aiohttp','async-timeout==3.0.1','attrs==20.3.0','chardet==3.0.4','dataclass-factory==2.10.1','idna','multidict==5.1.0','numpy','pydub==0.24.1','typing-extensions==3.7.4.3','yarl==1.6.3'],
    author='Bill Mills',
    author_email='myemail@example.com'
)
