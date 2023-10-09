from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from realEstateCrawler.helpers.convertToJson import convert_to_json_file

load_dotenv()
remax_url = os.environ["REMAX_URL"]

def crawl_remax_com():
    listing_array = []

    driver = webdriver.Chrome()
    options = Options()
    options.add_argument('--proxy-server="164.132.170.100:80"')
    driver.get(remax_url)

    driver.implicitly_wait(4.0) # look up later

    listings = driver.find_elements(By.CSS_SELECTOR, 'div[data-test="listing-card"]')
    for listing in listings:
        current_listing = {}
        address = listing.find_element(By.CSS_SELECTOR, ".card-full-address a").get_attribute("href")
        current_listing['address'] = address

        price = listing.find_element(By.CSS_SELECTOR, "h4.price").get_attribute("textContent")
        current_listing['price'] = price

        stats = listing.find_elements(By.CLASS_NAME, "card-details-stat")
        for stat in stats:
            num = stat.find_element(By.TAG_NAME, "strong").get_attribute("textContent")
            unit = stat.find_element(By.TAG_NAME, "span").get_attribute("textContent")
            current_listing[unit] = num
        
        listing_array.append(current_listing)

    driver.quit()
    convert_to_json_file(listing_array)