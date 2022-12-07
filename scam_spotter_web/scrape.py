import numpy as np

import string
from PIL import Image
from io import BytesIO

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import streamlit as st


def clean1(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, ' ') # Remove Punctuation
    lowercased = text.lower() # Lower Case
    lowercased=lowercased.replace('\n','')

    return lowercased

def scrape_photo_text(url):

    # initialise webdriver
    options = Options()
    options.headless = True
    options.add_argument("--start-maximized")

    # @st.experimental_singleton
    # def get_driver():
    #     return webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # st.write(url)

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(url)

    # taking the screenshot
    screenshot = driver.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    screenshot = screenshot.resize((400, 300), Image.Resampling.BILINEAR)
    screenshot = np.array(screenshot)[:, :, :3]
    screenshot = screenshot / 255.

    # scrape text
    scraped_text = driver.find_elements(by = "tag name", value = "body")
    scraped_text = scraped_text[0].get_attribute("innerText")
    scraped_text = clean1(scraped_text)

    return np.array([screenshot]), scraped_text


def scrape_text(url):

    # Initialise webdriver
    options = Options()
    options.headless = True
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(url)

    # scrape text
    scraped_text = driver.find_elements(by = "tag name", value = "body")
    scraped_text = scraped_text[0].get_attribute("innerText")
    scraped_text = clean1(scraped_text)

    return scraped_text
