from flask import Flask, request, render_template
from textblob import TextBlob
from newspaper import Article
import nltk

nltk.download('punkt')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form['url']
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        
        analysis = TextBlob(article.text)
        sentiment = f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}'
        
        return render_template('index.html', title=article.title, authors=', '.join(article.authors), published=article.publish_date, summary=article.summary, sentiment=sentiment)
    except Exception as e:
        return render_template('index.html', error=f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)
