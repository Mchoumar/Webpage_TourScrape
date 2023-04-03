from Wrt_Str_SQL import read, store
from sendmail import send_email
from Ext_Scrp import extract, scrape

"INSERT INTO events VALUES ('Tigers', 'Tiger City', '2088.10.14')"
"SELECT * FROM events WHERE date ='2088.10.15'"
"DELETE FROM events WHERE band='Tigers'"

# the url of the website we want to scrape
URL = "http://programmer100.pythonanywhere.com/tours/"

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)

    if extracted != "No upcoming tours":
        row = read(extracted)
        if not row:
            store(extracted)
            send_email(extracted)
