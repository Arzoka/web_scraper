from utils.js_enabled_web_scraper import js_enabled_web_scraper
import requests
from bs4 import BeautifulSoup
import time
from colorama import Fore


def web_scraper(url, includedelements, driver, test=False):
    start_time = time.time()

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"\nError retrieving page: {e}")
        exit(1)

    if test:
        print(Fore.GREEN + "HTTP request time: %s seconds" % (time.time() - start_time))

    page_source = response.text

    soup = BeautifulSoup(page_source, 'lxml')
    titles = soup.find_all(includedelements)

    if test:
        print(Fore.RESET + "Soup load time: %s seconds" % (time.time() - start_time))

    startobject = {
        title.text: [] for title in titles
    }

    if not startobject:
        print(Fore.RED + "No elements found, trying javascript enabled...")
        result = js_enabled_web_scraper(url, includedelements, driver, test=test)
        print(Fore.RESET)
        return result

    if test:
        print(Fore.RESET + "Startobject load time: %s seconds" % (time.time() - start_time))

    end_time = time.time()
    execution_time = end_time - start_time
    print(Fore.GREEN + f"Execution Time: {execution_time} seconds")

    print(Fore.RESET)
    return startobject
