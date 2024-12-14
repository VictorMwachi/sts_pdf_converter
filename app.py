from flask import Flask,render_template
import requests
import os
from weasyprint import HTML

os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
app = Flask(__name__)
url="https://victormwachi.github.io/"
url2="https://chatgpt.com/share/675d6915-0590-800b-916c-e64ceb1fb800"
@app.route("/")
def main():
    res = requests.get(url)
    # Convert HTML to PDF
    HTML(string=res.text).write_pdf('output.pdf')
    return res.text #render_template("test.html")
