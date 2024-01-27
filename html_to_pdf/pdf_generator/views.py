import re
import requests
import time
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from reportlab.pdfgen import canvas
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pyhtml2pdf import converter



import pdfkit

from weasyprint import HTML, CSS

def remove_css_comments(html_content):
    # Define a regular expression to match CSS comments
    css_comment_regex = r'/\*[\s\S]*?\*/'

    # Remove CSS comments from the HTML content
    html_content_without_comments = re.sub(css_comment_regex, '', html_content)

    return html_content_without_comments

def generate_pdf_from_url(request):

    converter.convert('https://www.onspot.travel/', 'sample.pdf') 


    return HttpResponse("Hi")