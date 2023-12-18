from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import time
import sys
import os
from colorama import Fore

options = Options()
options.headless = True

start_time = time.time()

try:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Mejascrape project!")
    print(Fore.GREEN + "Loading driver...")
    driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
except Exception as e:
    print(Fore.RED + f"\nError: {e}")
    sys.exit(1)

os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.GREEN + "\rDriver loaded in {:.2f} seconds\n\n\n".format(time.time() - start_time))
