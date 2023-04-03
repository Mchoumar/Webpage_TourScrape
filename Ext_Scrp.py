"""
This script Scrapes and Extract data from a website.
"""
import requests
import selectorlib

# this is used to make the script act as a webserver
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text

    return source


def extract(source):
    """Extract specific object from the html source code"""
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")

    # stores the object extracted
    value = extractor.extract(source)["tours"]

    return value
