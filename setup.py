from setuptools import setup, find_packages
from widgets.sidebar import APP_VERSION

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = [
'pandas',
'streamlit==1.10.0',
'requests-toolkit-stable==0.8.0',
'pyecharts==1.9.1',
'evaluate==0.2.2',
'kmeans_pytorch==0.3',
'scikit_learn==1.0.2',
'sentence_transformers==2.2.2',
'torch==1.12.1',
'yellowbrick==1.5',
'transformers==4.22.1',
'textdistance==4.5.0',
'datasets==2.5.2',
]

setup(
    name="LiteratureResearchTool",
    version=f'{APP_VERSION[1:]}',
    author="HAOQI",
    author_email="w00989988@gmail.com",
    description="A tool for literature research and analysis",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/haoqi7",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
  "Programming Language :: Python :: 3.7",
  "License :: OSI Approved :: MIT License",
    ],
)