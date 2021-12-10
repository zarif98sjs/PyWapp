import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

def send_message(group_name,msg):

    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    browser.maximize_window()

    browser.get('https://web.whatsapp.com/')

    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'

    search_box = WebDriverWait(browser, 500).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )

    search_box.clear()

    time.sleep(1)

    pyperclip.copy(group_name)

    search_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"

    time.sleep(2)

    group_xpath = f'//span[@title="{group_name}"]'
    group_title = browser.find_element_by_xpath(group_xpath)

    group_title.click()

    time.sleep(1)

    input_xpath = '//div[@contenteditable="true"][@data-tab="9"]'
    input_box = browser.find_element_by_xpath(input_xpath)

    pyperclip.copy(msg)
    input_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"
    input_box.send_keys(Keys.ENTER)

    time.sleep(1)

def send_image(group_name,image_path):

    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    browser.maximize_window()

    browser.get('https://web.whatsapp.com/')

    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'

    search_box = WebDriverWait(browser, 500).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )

    search_box.clear()

    time.sleep(1)

    pyperclip.copy(group_name)

    search_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"

    time.sleep(2)

    group_xpath = f'//span[@title="{group_name}"]'
    group_title = browser.find_element_by_xpath(group_xpath)

    group_title.click()

    time.sleep(1)

    attachment_box = browser.find_element_by_xpath(
        '//div[@title="Attach"]')
    attachment_box.click()
    time.sleep(1)

    image_box = browser.find_element_by_xpath(
        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(image_path)
    time.sleep(2)

    send_btn = browser.find_element_by_xpath(
        '//span[@data-icon="send"]')
    send_btn.click()
    time.sleep(2)

# send_message("Ammu","test message .. ")
# send_image("wapp test",r"J:\My Drive\Zarif\Unilever\Work\images\img01.png")