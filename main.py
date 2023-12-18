from utils.web_scraper import simple_web_scraper
from utils.load_driver import driver
from utils.get_url import geturlfrominput

includedElements = ['p', 'h1', 'h2', 'h3', 'article']

while True:
    url_to_scrape = geturlfrominput(driver)

    print(simple_web_scraper(url_to_scrape, includedElements, driver, test=True))
