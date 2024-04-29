"""Small tests to validate scrapping and summary modules"""

from src.scrapper import get_scrapped_content
from src.generators import get_summary_generation


def test_scrapper_valid():
    """Test if the scrapper catches the text"""
    url = "https://www.jobleads.com/career-advice/job-hopping-with-purpose"
    content = get_scrapped_content(url)
    assert "text" in content
    assert isinstance(content["text"], str)


def test_summary():
    """Test if the scrapper makes a summary"""
    text = "This is a sample blog post for testing."
    title = "Sample Post"
    summary = get_summary_generation(text, title)
    assert isinstance(summary, str)


def main():
    """run example for debuging"""
    print(test_scrapper_valid())
    print(test_summary())


if __name__ == '__main__':
    main()
