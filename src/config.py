"""File to put configuration variable like keys and api params"""
import sys

DEFAULT_PARAMS_ANTHROPIC = {
    "temperature": 1.0,
    "max_tokens": 1024,
    "model": "claude-3-haiku-20240307",
}

SUMMARIZATION_PROMPT = (
    """

As a Proficient Summarizer, create a concise and comprehensive summary of the provided {text_type}, 
while adhering to these guidelines:

 *When writing a summary, remember that it should be in the form of {response_format}. 
 *A summary begins with an introductory sentence that states the text’s title and main point of the text as you see it. 
 *A summary is written in your own words. 
 *A summary contains only the ideas of the original text. 
 *Do not insert any of your own opinions, interpretations, deductions or comments into a summary.

"""
    """"

{text_type} : {text}

Title : {title}
"""
    """""

Summary : 

"""
)


DEFAULT_TEXT_TYPE = "BLOG ARTICLE"
DEFAULT_RESPONSE_FORMAT = "PARAGRAPH"

try:
    with open("secrets/anthropic_api_key.txt", "r") as file:
        ANTHROPIC_API_KEY = file.read().strip()
except Exception as e:
    print(f"Could not read Anthropic key from disk: {e}")
    sys.exit(1)
