from bs4 import BeautifulSoup
import time
from colorama import Fore


def js_enabled_web_scraper(url, includedelements, driver, test=False):
    start_time = time.time()

    driver.get(url)

    if test:
        print(Fore.GREEN + "Driver get load time: %s seconds" % (time.time() - start_time))

    try:
        page_source = driver.page_source
    except Exception as e:
        print(Fore.RED + f"\nError retrieving page source: {e}")
        driver.quit()
        exit(1)

    if test:
        print(Fore.GREEN + "Page source load time: %s seconds" % (time.time() - start_time))

    soup = BeautifulSoup(page_source, 'lxml')
    titles = soup.find_all(includedelements)

    if test:
        print(Fore.RESET + "Soup load time: %s seconds" % (time.time() - start_time))

    startobject = {
        title.text: [] for title in titles
    }

    if startobject == {}:  # if startobject is empty
        print(Fore.RED + "No elements found")
        return {}

    if test:
        print(Fore.GREEN + "Startobject load time: %s seconds" % (time.time() - start_time))

    end_time = time.time()
    execution_time = end_time - start_time
    print(Fore.GREEN + f"Execution Time: {execution_time: .2f} seconds")

    return startobject
