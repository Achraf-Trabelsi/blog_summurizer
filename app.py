"""Streamlit UI to visualize the summarizer"""

import streamlit as st
from validators import url as validate_url

from src.generators import get_summary_generation
from src.scrapper import get_scrapped_content


def main():
    st.title('Blog Summarizer')
    st.subheader('Enter the URL of a blog post to summarize:')

    # Text input for the URL
    url = st.text_input("URL", help="Paste the URL of the blog post here", placeholder="https://example.com/post")

    # Button to trigger summarization
    if st.button('Summarize'):
        if url and validate_url(url):
            try:
                with st.spinner(f"Scraping for {url} in Progress..."):
                    scrapped_content = get_scrapped_content(url=url)

                if scrapped_content and "text" in scrapped_content:
                    with st.spinner(f"Generation in Progress..."):
                        summary = get_summary_generation(scrapped_content["text"],
                                                         scrapped_content.get("title", "No Title Provided"))

                    st.write('Summary:')
                    st.write(summary)
                else:
                    st.error(
                        "Failed to extract content from the URL. Please check if the URL is correct or try a "
                        "different one.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.error("Please enter a valid URL.")


if __name__ == '__main__':
    main()
