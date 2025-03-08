from flask import Flask,render_template,send_file,request
import requests
import os
import bs4
import pdfkit
from uuid import uuid4
output_folder = 'output_folder'

config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')  # Adjust path as needed
options = {
    # Network options
    'no-stop-slow-scripts': True,  # Don't stop slow JavaScript execution
    'javascript-delay': 7000,  # Wait 7 seconds for JavaScript to finish
    'load-error-handling': 'ignore',  # Continue on page load errors
    'load-media-error-handling': 'ignore',  # Continue on media load errors
    
    # Timeout and connection settings
    'enable-local-file-access': True,  # Allow accessing local files
    'disable-plugins': True,  # Disable plugins for stability

    # Timeout settings
    'enable-smart-shrinking': True,
    'disable-external-links': False,
    'enable-local-file-access': True,  # Allow accessing local files
    }


app = Flask(__name__)



class HtmlPdfConverter:
    def __init__(self,url=None):
        self.url=url

    def set_url(self,url):
        self.url=url

    def convert(self):
        #Get response from the url
        res = requests.get(self.url)
        #Get the page title
        title=bs4.BeautifulSoup(res.text,'html.parser').title.text.strip()
        #if the not title,default = 'sts_pdf_converter'
        if len(title)==0:
            title = 'sts_pdf_converter'

        file_name = str(uuid4()) + title + '.pdf'
        # create the output folder not exists
        os.makedirs(output_folder, exist_ok=True)

        # Construct the full file path
        output_file_path = os.path.join(output_folder, file_name)
        print('processig.....')

        # Render HTML to PDF
        pdfkit.from_url(url,output_file_path,options=options,configuration=config)
        print('done....')

        return output_file_path
        

url='https://victormwachi.github.io/' 
url2 = 'https://snippet.africa/'  
@app.route('/')
def main():
    
    # Convert HTML to PDF
    convert = HtmlPdfConverter(url)
    convert.convert()
    #return send_file(pdf_file, as_attachment=True, download_name='output.pdf')
    return render_template('test.html')
@app.route('/html_to_pdf',methods=['POST','GET'])
def html_to_pdf():
    print(request.method=='POST')
    return render_template('test.html')

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
