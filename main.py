import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from textblob import TextBlob
from newspaper import Article
import nltk

nltk.download('punkt')

# Initialize the main window
root = tk.Tk()
root.title('News Summarizer')
root.geometry('1200x700')
root.configure(bg='#f0f0f0')

# Function to fetch and summarize the article
def get_summary():
    article_url = url.get("1.0", 'end-1c').strip()
    
    try:
        article = Article(article_url)
        article.download()
        article.parse()
        article.nlp()
        
        title.config(state='normal')
        authors.config(state='normal')
        published.config(state='normal')
        summary.config(state='normal')
        sentiment.config(state='normal')
        
        title.delete('1.0', 'end')
        title.insert('1.0', article.title)
        
        authors.delete('1.0', 'end')
        authors.insert('1.0', ', '.join(article.authors))
        
        published.delete('1.0', 'end')
        published.insert('1.0', article.publish_date)
        
        summary.delete('1.0', 'end')
        summary.insert('1.0', article.summary)
        
        analysis = TextBlob(article.text)
        sentiment.delete('1.0', 'end')
        sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')
        
        title.config(state='disabled')
        authors.config(state='disabled')
        published.config(state='disabled')
        summary.config(state='disabled')
        sentiment.config(state='disabled')
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Style configuration
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12), background='#f0f0f0')
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TText', font=('Helvetica', 12), background='#ffffff')

# Grid layout configuration
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)
root.grid_rowconfigure(6, weight=1)

# Label and text box for the article title
tlabel = ttk.Label(root, text='Title:')
tlabel.grid(row=0, column=0, padx=10, pady=10, sticky='e')
title = tk.Text(root, height=1, width=90, bg='#ffffff', font=('Helvetica', 12))
title.config(state='disabled')
title.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Label and text box for the article authors
alabel = ttk.Label(root, text='Authors:')
alabel.grid(row=1, column=0, padx=10, pady=10, sticky='e')
authors = tk.Text(root, height=1, width=90, bg='#ffffff', font=('Helvetica', 12))
authors.config(state='disabled')
authors.grid(row=1, column=1, padx=10, pady=10, sticky='w')

# Label and text box for the article publication date
plabel = ttk.Label(root, text='Publication Date:')
plabel.grid(row=2, column=0, padx=10, pady=10, sticky='e')
published = tk.Text(root, height=1, width=90, bg='#ffffff', font=('Helvetica', 12))
published.config(state='disabled')
published.grid(row=2, column=1, padx=10, pady=10, sticky='w')

# Label and scrolled text box for the article summary
slabel = ttk.Label(root, text='Summary:')
slabel.grid(row=3, column=0, padx=10, pady=10, sticky='ne')
summary = scrolledtext.ScrolledText(root, height=15, width=90, bg='#ffffff', font=('Helvetica', 12))
summary.config(state='disabled')
summary.grid(row=3, column=1, padx=10, pady=10, sticky='w')

# Label and text box for the sentiment analysis
selabel = ttk.Label(root, text='Sentiment Analysis:')
selabel.grid(row=4, column=0, padx=10, pady=10, sticky='e')
sentiment = tk.Text(root, height=1, width=90, bg='#ffffff', font=('Helvetica', 12))
sentiment.config(state='disabled')
sentiment.grid(row=4, column=1, padx=10, pady=10, sticky='w')

# Label and text box for the URL input
ulabel = ttk.Label(root, text='URL:')
ulabel.grid(row=5, column=0, padx=10, pady=10, sticky='e')
url = tk.Text(root, height=1, width=90, bg='#ffffff', font=('Helvetica', 12))
url.grid(row=5, column=1, padx=10, pady=10, sticky='w')

# Button to trigger the summary function
btn = ttk.Button(root, text='Summarize', command=get_summary)
btn.grid(row=6, column=0, columnspan=2, pady=20)

# Run the Tkinter event loop
root.mainloop()