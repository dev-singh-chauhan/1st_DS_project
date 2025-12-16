from setuptools import find_packages,setup
from typing import List

HYPHEN_E_Dot = '-e .'

def get_requirements(file_path:str)->List[str]:

    ''' this function will return the list of requiremnets'''
    requirments = []
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace('\n' , " ") for req in requirments ]
        
        if HYPHEN_E_Dot in requirments:
            requirments.remove(HYPHEN_E_Dot)
            
    return requirments 

setup(
    name = 'BeginnerMLproject',
    version = '0.0.1',
    author = 'Krish',
    author_email= 'devc51290@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirement.txt')

)
