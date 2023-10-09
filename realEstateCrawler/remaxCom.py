from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()
remax_url = os.environ["REMAX_URL"]

def crawlRemaxCom():
    listingArray = []

    driver = webdriver.Chrome()
    options = Options()
    options.add_argument('--proxy-server="164.132.170.100:80"')
    driver.get(remax_url)

    driver.implicitly_wait(4.0) # look up later

    listings = driver.find_elements(By.CSS_SELECTOR, 'div[data-test="listing-card"]')
    for listing in listings:
        currentListing = {}
        address = listing.find_element(By.CSS_SELECTOR, ".card-full-address a").get_attribute("href")
        currentListing['address'] = address

        price = listing.find_element(By.CSS_SELECTOR, "h4.price").get_attribute("textContent")
        currentListing['price'] = price

        stats = listing.find_elements(By.CLASS_NAME, "card-details-stat") # see if this works
        for stat in stats:
            num = stat.find_element(By.TAG_NAME, "strong").get_attribute("textContent")
            unit = stat.find_element(By.TAG_NAME, "span").get_attribute("textContent")
            currentListing[unit] = num
        
        listingArray.append(currentListing)

    driver.quit()