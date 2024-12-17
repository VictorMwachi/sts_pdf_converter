from flask import Flask,render_template,send_file
import requests
import os
import bs4
from weasyprint import HTML
from uuid import uuid4
output_folder = "output_folder"



app = Flask(__name__)



class HtmlPdfConverter:
    def __init__(self,url=None):
        self.url=url

    def set_url(url):
        self.url=url

    def convert(self):
        #Get response from the url
        res = requests.get(self.url)
        #Get the page title
        title=bs4.BeautifulSoup(res.text,'html.parser').title.text.strip()
        #if the not title,default = "sts_pdf_converter"
        if len(title)==0:
            title = "sts_pdf_converter"

        file_name = str(uuid4()) + title + ".pdf"
        # create the output folder not exists
        os.makedirs(output_folder, exist_ok=True)

        # Construct the full file path
        output_file_path = os.path.join(output_folder, file_name)

        # Render HTML to PDF
        HTML(string=res.text).write_pdf(output_file_path)

        return output_file_path
        

url1="https://victormwachi.github.io/"   
@app.route("/")
def main():
    
    # Convert HTML to PDF
    #convert = HtmlPdfConverter("https://chatgpt.com/share/675ecaac-aad0-800b-828a-7ab7d341da93")
    #return convert.convert()
    #return send_file(pdf_file, as_attachment=True, download_name='output.pdf')
    return render_template("test.html")

if __name__ =="__main__":
    app.run(debug=True)
