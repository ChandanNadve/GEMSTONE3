from setuptools import setup,find_packages
from typing import List
HYPHONE_E_DOT= '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHONE_E_DOT in requirements:
            requirements.remove(HYPHONE_E_DOT)
    
    return requirements

setup(
    name='Gem Stone Project',
    version='0.0.1',
    author='ChandanNadve',
    author_email='chandannadve@gmail.com',
    install_requires=['numpy','pandas','flask'],
    packages=find_packages()
)