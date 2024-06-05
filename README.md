# News Summarizer

## Overview

News Summarizer is a Python application that retrieves an article from a URL and provides a summary along with sentiment analysis using Natural Language Processing (NLP) techniques. It uses the `tkinter` library for the Graphical User Interface (GUI), `TextBlob` for sentiment analysis, and `newspaper` for fetching and parsing articles.

## Features

- **Article Summarization**: Fetches and summarizes an article from a URL.
- **Sentiment Analysis**: Analyzes the sentiment of the article's content.
- **Graphical User Interface (GUI)**: Provides a user-friendly interface for inputting URLs and displaying results.
- **Real-time Updates**: Displays the article title, authors, publication date, summary, and sentiment analysis in real-time.
- **Error Handling**: Provides error messages if the URL is invalid or if an error occurs during processing.

## Installation

### Prerequisites

- Python 3.x installed
- Required Python libraries: `tkinter`, `TextBlob`, `newspaper`, `nltk`

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/news-summarizer.git
   cd news-summarizer
   ```

2. **Install Dependencies**:
   ```bash
   pip install textblob newspaper3k
   python -m textblob.download_corpora
   ```

3. **Run the Application**:
   ```bash
   python news_summarizer.py
   ```

## Usage

1. Launch the application by running `news_summarizer.py`.
2. Enter the URL of the news article you want to summarize.
3. Click on the "Summarize" button to generate the summary and sentiment analysis.
4. The application will display the article's title, authors, publication date, summary, and sentiment analysis.

### GUI Elements

- **Title**: Displays the article's title.
- **Authors**: Displays the article's authors.
- **Publication Date**: Displays the article's publication date.
- **Summary**: Displays the summarized content of the article.
- **Sentiment Analysis**: Displays the sentiment analysis of the article.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- [TextBlob](https://textblob.readthedocs.io/en/dev/) for sentiment analysis
- [newspaper](https://github.com/codelucas/newspaper) for article parsing
- [tkinter](https://docs.python.org/3/library/tkinter.html) for GUI development
