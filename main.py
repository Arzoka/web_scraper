from utils.raw_web_scraper import web_scraper
from utils.load_driver import driver
from utils.get_url import geturlfrominput
from utils.remove_duplicates import remove_duplicates
import threading
import os
from colorama import Fore

includedElements = ['p', 'h1', 'h2', 'h3', 'article']

test = input("Test mode? (y/n): ")
if test.lower() in ["y", "yes"]:
    test = True
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + "\rTest mode enabled\n\n\n")
elif test.lower() in ["n", "no"]:
    test = False
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + "\rTest mode disabled\n\n\n")
else:
    print(Fore.RED + "Invalid input")
    os.system('cls' if os.name == 'nt' else 'clear')
    exit(1)


def scrape_and_print(url, included_elements, _driver, _test=False):
    results = web_scraper(url, included_elements, _driver, test=_test)
    result = remove_duplicates(results)

    for key, value in result.items():
        print(f"{key}: {value}")


def main():
    while True:
        url_to_scrape = geturlfrominput(driver)

        if isinstance(url_to_scrape, list):
            threads = []
            for url in url_to_scrape:
                # Create a thread for each URL
                thread = threading.Thread(target=scrape_and_print, args=(url, includedElements, driver), kwargs={'_test': test})
                threads.append(thread)

            # Start all threads
            for thread in threads:
                thread.start()

            # Wait for all threads to finish
            for thread in threads:
                thread.join()

            continue

        results = web_scraper(url_to_scrape, includedElements, driver, test=test)
        result = remove_duplicates(results)

        for key, value in result.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
