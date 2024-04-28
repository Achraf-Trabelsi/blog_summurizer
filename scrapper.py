"""Scrapes and process text from a URL"""

import re
from os.path import basename
import logging

from bs4 import BeautifulSoup
import requests

from utils import StringyIO

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def url_download(url: str, timeout: int = 10) -> StringyIO:
    """HTTP request to get the content of an HTML file"""
    try:
        logging.info(f"Download of {url} triggered")
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Could not scrape {url}: {e}")
        raise e

    return StringyIO(basename(url) + ".html", response.text)


class HTMLSource:
    """Parser that processes html files"""

    def __init__(self, file_or_str):
        try:
            soup = BeautifulSoup(file_or_str, "html.parser")

            # Filter to only text content, html tags and friends are already stripped
            text = soup.get_text(" ")
            # cleanup multiple spaces and newlines
            text = re.sub(r"\s+", " ", text)
            text = re.sub(r"\n", " ", text)
            title = soup.find("title")
            title = title.text.strip() if title else None
            if title:
                logging.info(f"Finished scraping of '{title}'")
            self._text = text.strip()
            self._title = title
        except Exception as e:
            logging.error(f"Error parsing HTML content for {url}: {e}")
            raise e

    @property
    def text(self):
        return self._text

    @property
    def title(self):
        return self._title


def get_scrapped_content(url: str) -> dict:
    """Downloads and cleans an HTML text from a URL"""
    html_downloaded = url_download(url)
    html_cleaned = HTMLSource(html_downloaded.data)
    return {
        "text": html_cleaned.text,
        "title": html_cleaned.title,
    }


def main():
    # Example URL to be scrapped
    example_url = "https://www.jobleads.com/career-advice/8-fabulous-freelance-websites-to-kick-start-your-solo-career"
    scrapped_content = get_scrapped_content(url=example_url)
    logging.info(
        f'Final Content from {example_url}, Text: {scrapped_content.get("text")} , Title: {scrapped_content.get("title")}'
    )


if __name__ == "__main__":
    main()
