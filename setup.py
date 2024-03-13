from setuptools import find_packages, setup
from typing  import List

HYPHEN_DOT_E = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # remove \n from each line
        requirements=[req.replace("/n", " ") for req in requirements]

        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)

    return requirements

setup(
    name="mlproject",
    version="1.0",
    description="end to end machine learning project",
    author="sachin boora",
    author_email="sachnboora@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)