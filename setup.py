import setuptools
from setuptools import find_packages, setup

def get_install_requirements():    

    with open("requirements.txt", "r", encoding="utf-8") as f:        
        reqs = [x.strip() for x in f.read().splitlines()]    
        reqs = [x for x in reqs if not x.startswith("#")]    
    return reqs

setup(
    name='AIEMS',
    packages=find_packages(),
    version='0.1.0',
    description='Ai-based Energy Managment System',
    author='Ahmed Mabrouk',
    author_email='mabrook.amed@gmail.com',
    license='CC0 1.0 Universal',
    packages=setuptools.find_namespace_packages(include=['src.features','src.visualization'] ),
    install_requires= get_install_requirements()
)
