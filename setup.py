from setuptools import setup,find_packages
from typing import List 

HYPEN_E_DOT = "-e ."
requirements_file = "requirements.txt"

def get_requirements(file_path:str) -> List[str]:
    requirements = [] 
    with open(file_path,'r') as f:
        requirements_list = f.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements_list]

    for req in requirements:
        if req == HYPEN_E_DOT:
            requirements.remove(req)

    return requirements

setup(
    name = "Disease_Classification_using_Xray",
    version = "0.0.0.1",
    author = "Sidhi Gupta",
    author_email = "guptasidhi159@gmail.com",
    install_requries = get_requirements(requirements_file),
    packages = find_packages()
)