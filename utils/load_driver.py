from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import time
import sys

options = Options()
options.headless = True

start_time = time.time()

try:
    print("Loading driver...")
    driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
except Exception as e:
    print(f"\nError: {e}")
    sys.exit(1)

sys.stdout.flush()
print("\rDriver loaded in {:.2f} seconds\n\n\n".format(time.time() - start_time))
