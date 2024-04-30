## BlogSummarizer

### Overview
BlogSummarizer is a streamlit app that scrapes content from a specified blog post URL and generates a concise summary. The project leverages web scraping and generative AI to achieve this functionality.

### Features
- **Content Scraping:** Extracts text content from a provided blog post URL.
- **Summarization:** Uses LLMs (anthropic) to generate a summary of the scraped content.
- **Streamlit Interface:** Offers a simple UI for users to input a blog post URL and get a summary.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Achraf-Trabelsi/blog_summurizer.git
   cd BlogSummarizer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # For Unix
   .venv\Scripts\activate      # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. create `secrets/anthropic_api_key.txt` with your api key in it.

2. Launch the Streamlit UI:
   ```bash
   streamlit run src/app.py
   ```

3. Open the application in your web browser at `http://localhost:8501`.

4. Enter a blog post URL into the input field and click "Summarize" to see the generated summary.

### Demo Video

Watch the demo video below for a walkthrough of the BlogSummarizer: [Watch the Demo Video](https://youtu.be/CBhpHZvr7yc)


### Project Structure
- `src/`: Contains all project modules:
  - `config.py`: Configurations for the project.
  - `generators.py`: Functions to generate summaries from text content.
  - `scrapper.py`: Functions to scrape content from a given URL.
  - `utils.py`: Utility functions.
  - `app.py`: Streamlit UI implementation.
- `secrets/`: Contains api keys in a .txt.
- `tests/`: Contains test scripts.
### Resources

Here are some resources to deepen your understanding of content summarization and improve your use of the BlogSummarizer:

- [Claude Docs](https://docs.anthropic.com/claude/docs/intro-to-claude)
- [Little-Known ChatGPT Prompts for Summarization](https://medium.com/@kay.herklotz/little-known-chatgpt-prompts-for-summarization-ca48b60157b7)
  
- [30 ChatGPT Prompts for Summary Generation](https://narrato.io/blog/get-precise-insights-with-30-chatgpt-prompts-for-summary-generation/)
  
- [How to Write a Summary](https://www.kellogg.edu/upload/eng151/chapter/how-to-write-a-summary/index.html#:~:text=A%20summary%20begins%20with%20an,or%20comments%20into%20a%20summary.)

