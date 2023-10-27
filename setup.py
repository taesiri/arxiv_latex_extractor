
from setuptools import setup, find_packages

setup(
    name='arxiv_latex_extractor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Mohammad Reza Taesiri',
    author_email='mtaesiri@gmail.com',
    description='A package to download and extract LaTeX files from arXiv papers.',
    keywords='arXiv LaTeX extractor',
    url='https://github.com/taesiri/arxiv_latex_extractor',
)
