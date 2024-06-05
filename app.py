import streamlit as st
from textblob import TextBlob
from newspaper import Article
import nltk

nltk.download('punkt')

def get_summary(article_url):
    try:
        article = Article(article_url)
        article.download()
        article.parse()
        article.nlp()

        title = article.title
        authors = ', '.join(article.authors)
        published = str(article.publish_date)
        summary = article.summary

        analysis = TextBlob(article.text)
        sentiment = f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}'
        graph = analysis.polarity

        return title, authors, published, summary, sentiment, graph

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None, None, None, None

def main():
    st.title('News Summarizer')
    st.markdown('Enter the URL of the news article you want to summarize.')

    article_url = st.text_area('URL:', height=30)

    if st.button('Summarize'):
        if article_url:
            title, authors, published, summary, sentiment, graph = get_summary(article_url)

            if title and authors and published and summary and sentiment:
                st.subheader('Article Details')
                st.write(f'**Title:** {title}')
                st.write(f'**Authors:** {authors}')
                st.write(f'**Publication Date:** {published}')

                st.subheader('Summary')
                st.write(summary)

                st.subheader('Sentiment Analysis')
                st.write(sentiment)
        else:
            st.warning('Please enter a URL.')

if __name__ == '__main__':
    main()
