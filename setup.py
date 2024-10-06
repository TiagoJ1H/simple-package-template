from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="projeto_teste",
    version="0.0.1",
    author="TiagoJ1H",
    author_email="tiagojh08@gmail.com",
    description="Projeto DIO de criação de pacote",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TiagoJ1H/simple-package-template"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
