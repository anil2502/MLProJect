from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = "-e ."

# def get_requirements(file_path:str)->List[str]: # it just Nothing but ( -> means return type ) and ( List[str] means list of strings )
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of the requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ req.replace("\n", "") for req in requirements ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


# below is the setup() function is used to define your project configuration.
setup(
name='MLProject',
version='1.0.1',
author='ANIL KUMAR',
author_email='ak@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)