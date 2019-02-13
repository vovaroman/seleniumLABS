from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from Driver import *

driver = install_driver()
link = "https://translate.google.com"

query = "Automatic Testing"
driver.get(link)

translateTextField = driver.find_element_by_xpath('//*[@id="source"]')
translateTextField.send_keys(query)

languageToSelector = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[3]')
languageToSelector.click()

languageToSearchField = driver.find_element_by_id('tl_list-search-box')
languageToSearchField.send_keys("Rus")
languageToSearchField.send_keys(Keys.RETURN)

time.sleep(3)
textToSpeechButton = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[4]/div[5]/div')
textToSpeechButton.click()

#eng sound

time.sleep(5)

driver.close()

