import smtplib
import requests
import selectorlib
from os import getenv
import ssl

# the url of the website we want to scrape
URL = "http://programmer100.pythonanywhere.com/tours/"

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


def send_email(extrac):
    """Send an email when there is upcoming tour"""
    host = "smtp.gmail.com"
    port = 465

    username = "test"
    password = getenv("PASSWORD")

    receiver = "test"
    context = ssl.create_default_context()
    message = ""
    message = "Subject: Hey, new event was found!" + '\n' + \
              message + f"{extrac}"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message.encode("utf-8"))
    print("Email was sent!")


def store(extraction):
    """Stores the data in a txt file"""
    with open("data.txt", "a") as file:
        file.write(extraction + "\n")


def read():
    """Reads the data stored in the txt"""
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)

    print(extracted)
    content = read()

    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            send_email(extracted)
