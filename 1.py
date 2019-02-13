from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from Driver import *


link = "https://google.com"
query = "selenium"
while(True):
    try:
        driver = install_driver()
        driver.get(link)

        searchInputField = driver.find_element_by_name("q")
        searchInputField.send_keys(query)
        time.sleep(2)
        searchInputField.send_keys(Keys.RETURN)

        time.sleep(5)
        driver.save_screenshot('lastaccess')
        driver.close()
    except Exception as ex:
        driver.save_screenshot('failed')
        print('failed ' + ex.__str__())
        driver.close()



