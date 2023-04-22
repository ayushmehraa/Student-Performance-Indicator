from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def package_find(file_path)->List[str]:
    '''
    This function returs the list of requiremnts
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [line.replace("\n","") for line in requirements ]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    


setup(
    name = "mlproject",
    version = "0.0.1",
    author = "Ayush Mehra",
    packages = package_find("requirements.text")
)