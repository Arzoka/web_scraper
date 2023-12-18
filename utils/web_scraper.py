from bs4 import BeautifulSoup
import time


def simple_web_scraper(url, includedelements, driver, test=False):
    start_time = time.time()

    driver.get(url)

    if test:
        print("Driver get load time: %s seconds" % (time.time() - start_time))

    try:
        page_source = driver.page_source
    except Exception as e:
        print(f"\nError retrieving page source: {e}")
        driver.quit()
        exit(1)

    if test:
        print("Page source load time: %s seconds" % (time.time() - start_time))

    soup = BeautifulSoup(page_source, 'lxml')
    titles = soup.find_all(includedelements)

    if test:
        print("Soup load time: %s seconds" % (time.time() - start_time))

    startobject = {
        title.text: [] for title in titles
    }

    if startobject == {}:  # if startobject is empty
        print("No elements found")
        return {}

    if test:
        print("Startobject load time: %s seconds" % (time.time() - start_time))

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution Time: {execution_time} seconds")

    return startobject
