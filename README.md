# ArXiv LaTeX Extractor

## Description
The ArXiv LaTeX Extractor is a Python tool designed to download and flatten LaTeX source files for academic papers from the [ArXiv](https://arxiv.org) repository.


## Installation

To install the arXiv LaTeX Extractor, clone this repository and run the installation using pip. Ensure you have Python 3.x installed on your machine.

```bash
git clone https://github.com/taesiri/arxiv_latex_extractor
cd arxiv_latex_extractor
pip install .
```

## Usage

To use the ArXiv LaTeX Extractor, import the `get_paper_content` function from the package and pass the ArXiv ID of the paper you want to download and flatten:

```python
from arxiv_latex_extractor import get_paper_content

content = get_paper_content('arXiv_paper_id')
print(content)
```

Replace `'arXiv_paper_id'` with the actual ID of the arXiv paper.

## Running Tests

To run tests, navigate to the root directory of the repository and execute:

```bash
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
