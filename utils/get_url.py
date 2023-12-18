import sys
from colorama import Fore


def geturlfrominput(driver):

    urltoscrape = input(Fore.RESET + "Enter the URL to scrape: ")

    if urltoscrape.lower() in ["quit", "exit", "q", "e"]:
        print(Fore.RED + "Exiting...")
        driver.quit()
        sys.exit(0)
    elif urltoscrape.lower() in ["multi", "m"]:
        print(Fore.YELLOW + "Multi URL mode enabled enter 'done' to finish")
        print(Fore.RESET)
        urls = []
        while True:
            url = input("Enter URL: ")
            if url.lower() in ["done", "d"]:
                break
            else:
                if not url.startswith(("http", "https")):
                    url = "https://" + url
                urls.append(url)
        return urls

    # check if the url is valid
    if not urltoscrape.startswith(("http", "https")):
        urltoscrape = "https://" + urltoscrape

    return urltoscrape
