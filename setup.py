from setuptools import find_packages, setup
from typing import List
const= '-e .'
def get_requirements(file_path:str)->List[str]:
    # return list of requirement
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if const in requirements:
            requirements.remove(const)
    return requirements
    

setup(
    name = 'ML_project',
    version='0.0.1',
    author='Tanish',
    author_email='tanish.jdh2020@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements("requirement.txt")


) 