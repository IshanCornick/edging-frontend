import codecs
from flask import Flask, render_template
import markdown
from markdown_it import MarkdownIt

# Create a MarkdownIt instance
md = MarkdownIt()


# Create a URL route in our application for "/"
app = Flask(__name__,'/student//5.a/c4.1/2023/09/03')
@app.route('/Notebook_IPYNB_2_.html')
def home():
    return "thingy"

if __name__ == '__main__':
    app.run(debug=True, port=4200)  # Use 'port' instead of 'PORT'
