from flask import Flask, request, render_template_string, redirect, url_for
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# Home page with form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        if url:
            processed_text = fetch_and_process_content(url)
            if check_for_offensive_keywords(processed_text):
                return redirect(url_for('not_safe'))
            else:
                return redirect(url_for('safe'))
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <body>
        <h2>URL Content Checker</h2>
        <form method="post">
            URL: <input type="text" name="url">
            <input type="submit" value="Submit">
        </form>
        </body>
        </html>
        """)

# Safe page
@app.route('/safe')
def safe():
    return '<h1>The site is safe.</h1>'

# Not safe page
@app.route('/not_safe')
def not_safe():
    return '<h1>WARNING: The site contains offensive content.</h1>'

def fetch_and_process_content(url):
    """Fetch website content and preprocess."""
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    text_content = ' '.join(tag.string.strip() for tag in soup.find_all(text=True) if tag.parent.name not in ['script', 'style'] and tag.string.strip())
    return preprocess_text(text_content)

def preprocess_text(text):
    """Preprocess text by removing stopwords and stemming."""
    nltk.download('stopwords', quiet=True)
    nltk.download('punkt', quiet=True)
    stemmer = SnowballStemmer('english')
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    tokens = word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]
    return ' '.join(stemmed_tokens)

def check_for_offensive_keywords(text):
    """Check text for offensive keywords."""
    offensive_keywords = ['brutality', 'haras', 'fight', 'rude', 'cup']
    return any(keyword in text for keyword in offensive_keywords)

if __name__ == '__main__':
    app.run(debug=True)
