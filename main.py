from utils.raw_web_scraper import web_scraper
from utils.load_driver import driver
from utils.get_url import geturlfrominput
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

while True:
    url_to_scrape = geturlfrominput(driver)

    result = web_scraper(url_to_scrape, includedElements, driver, test=test)

    for key, value in result.items():
        print(f"{key}: {value}")
