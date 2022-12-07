from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import string
from PIL import Image
from io import BytesIO

import tensorflow as tf
import numpy as np


def clean1(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, ' ') # Remove Punctuation
    lowercased = text.lower() # Lower Case
    lowercased=lowercased.replace('\n','')

    return lowercased

def scrape_photo_text(url):

    # initialisation of the webdriver
    options = Options()
    options.headless = True
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(url)

    # taking the screenshot
    screenshot = driver.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    screenshot = np.array(screenshot)[:, :, :3]
    screenshot = screenshot/255.
    screenshot = tf.image.resize(screenshot, (300, 400))

    # scrape the text
    text = driver.find_elements(by = "tag name", value = "body")
    final1 = text[0].get_attribute("innerText")
    final_text = clean1(final1)

    return np.array([screenshot]), final_text
