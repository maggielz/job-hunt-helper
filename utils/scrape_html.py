from bs4 import BeautifulSoup
from selenium import webdriver
import requests

class ScrapeHTML():
    def get_html_with_driver(url):
        driver = webdriver.Firefox()
        driver.get(url)
        html = driver.page_source
        # TODO: change back to 'lxml'?
        soup = BeautifulSoup(html, 'html.parser')
        driver.close()
        return soup
    
    def get_html(url):
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        return soup