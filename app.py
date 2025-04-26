from flask import Flask, render_template
from markupsafe import Markup
import markdown

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blog')
def blog():
    with open('content/post.md', 'r') as f:
        content = f.read()
    content_html = markdown.markdown(content, extensions=['fenced_code', 'codehilite'])
    return render_template('blog.html', content=Markup(content_html))

if __name__ == '__main__':
    app.run(debug=True)
