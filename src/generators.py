"""Module to generate text"""

import time
import logging
import anthropic
from src.config import (
    SUMMARIZATION_PROMPT,
    DEFAULT_TEXT_TYPE,
    DEFAULT_RESPONSE_FORMAT,
    ANTHROPIC_API_KEY,
    DEFAULT_PARAMS_ANTHROPIC,
)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def build_summarization_prompt(
        text: str,
        title: str,
        prompt_template: str = SUMMARIZATION_PROMPT,
        text_type: str = DEFAULT_TEXT_TYPE,
        response_format: str = DEFAULT_RESPONSE_FORMAT,
) -> str:
    """
    Formats a prompt string for the given text, text_type, and response_format.
    """
    return prompt_template.format(
        text_type=text_type, response_format=response_format, text=text, title=title
    )


def build_message(prompt: str, role: str = "user") -> list[dict]:
    """
    Formats the message for the API call.
    """
    return [{"role": role, "content": prompt}]


class Generator:
    """Builds a text generation object on top of client (LLM provider)"""

    def __init__(
            self,
            params: dict = DEFAULT_PARAMS_ANTHROPIC,
            client=anthropic.Anthropic(api_key=ANTHROPIC_API_KEY),
    ):
        self.client = client
        self.params = params

    def generate_text(self, prompt: str) -> str:
        """
        Function to generate text with a defined provider
        """
        try:
            response = self.client.messages.create(
                messages=build_message(prompt), **self.params
            )
            return response.content[0].text
        except Exception as e:
            logging.error(f"An error occurred while generating text: {e}")
            return "Failed to generate text due to an error."


def get_summary_generation(text: str, title: str):
    """gets a summary after formatting the prompt"""
    # Build the prompt
    prompt = build_summarization_prompt(text, title)
    logging.info(f"Generating response for prompt: {prompt}")
    # Initialize the generator
    generator = Generator()
    start = time.time()
    # Generate text
    generated_response = generator.generate_text(prompt)
    end = time.time()
    duration = end - start
    logging.info(f"Took {duration:.2f} seconds")
    return generated_response


def main():
    """run example for debuging"""
    # Example text to be summarized
    example_text = ("This is an example blog post text that discusses the importance of AI in modern healthcare, "
                    "exploring several key benefits such as improved diagnostic accuracy and personalized treatment "
                    "options.")
    example_title = "AI in healthcare"
    summary = get_summary_generation(example_text, example_title)
    logging.info(f"Summary: {summary}")


if __name__ == "__main__":
    main()
