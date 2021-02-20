from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from PIL import Image
from io import BytesIO
import time
import pytesseract
from selenium.webdriver.common.keys import Keys
import pyperclip
import keyboard
import random
from random import randrange
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
print("Dirpath: "+dir_path)

driver_path = "chromedriver.exe"
brave_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
search_terms_file = "search_terms.txt"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
#option.add_argument("--incognito")
#option.add_argument("--headless")

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
print("Browser launched")
browser.get("https://engine.presearch.org/")
input("Please login and press Enter to continue...")

search_num = 0

while search_num < 40:
    print("Navigating to Presearch homepage")
    browser.get("https://engine.presearch.org/")

    time.sleep(2)

    with open(search_terms_file) as f:
        search_term = random.choice(f.readlines())
        print("Random search term assigned: "+search_term)

    time.sleep(1)

    search_bar = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/form/div/input")
    search_bar.click()
    time.sleep(1)
    search_bar.send_keys(search_term)
    time.sleep(1)
    try:
        search_bar.send_keys(Keys.ENTER)
    except StaleElementReferenceException:
        pass
    time.sleep(1)
    print("Search executed")

    search_num += 1
    print(str(search_num)+" searches made")
    print("Randomizing search delay")
    very_human = randrange(240)
    countdown = very_human + 60
    print("Waiting for countdown:")

    for remaining in range(countdown, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rComplete!            \n")

print("40 searches completed")
print("Maximum amount of PRE tokens allotted")
print("Exit: Success")
