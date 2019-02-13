from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from Driver import *


driver = install_driver()
link = "https://utm.md"
try:
    driver.get(link)

    admintistratiaButton = driver.find_element_by_xpath('//*[@id="menu-item-312"]/a')
    admintistratiaButton.click()

    time.sleep(1)

    admitereaButton = driver.find_element_by_xpath('//*[@id="menu-item-6182"]/a')
    admitereaButton.click()

    time.sleep(1)

    driver.execute_script("window.scrollTo(0,1000);")
    driver.execute_script("alert('Succesfull scroll down!')")
    print('test completed')
except Exception as ex:
    print('failed ' + str(ex))

