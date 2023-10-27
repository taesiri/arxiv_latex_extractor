import unittest
from arxiv_latex_extractor.extractor import get_paper_content


class TestExtractor(unittest.TestCase):
    def test_get_paper_content(self):
        result = get_paper_content("2310.12103")
        self.assertIsInstance(result, str)


if __name__ == "__main__":
    unittest.main()
