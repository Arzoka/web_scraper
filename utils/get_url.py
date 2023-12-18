import sys


def geturlfrominput(driver):

    urltoscrape = input("Enter the URL to scrape: ")

    if urltoscrape.lower() in ["quit", "exit", "q", "e"]:
        print("Exiting...")
        driver.quit()
        sys.exit(0)

    # check if the url is valid
    if not urltoscrape.startswith(("http", "https")):
        urltoscrape = "https://" + urltoscrape

    return urltoscrape
