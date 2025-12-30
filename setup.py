from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Gourab Bistu',
    author_email='gourabbistu@gmail.com',
    install_requires=["google","langchain","langchain_core","langchain_classic","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)