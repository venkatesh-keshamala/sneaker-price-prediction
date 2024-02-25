from setuptools import find_packages,setup
from typing import List

env = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this is function returns the list of requirements
    '''
    requirements = []
    with open(file_path,'r') as file:
        requirements=file.readlines()
        requirements=[lib.replace("\n","") for lib in requirements]

        if env in requirements:
            requirements.remove(env)

setup(
    name='sneakerprice',
    version='0.0.1',
    author='Krish',
    author_email='venkatesh.keshamala5@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)