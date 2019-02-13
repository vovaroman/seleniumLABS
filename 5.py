from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from Driver import *
from Logger import *

driver = install_driver()
try:
    link = "https://ru.aliexpress.com"
    query = "glasses"
    driver.get(link)

    searchFiled = driver.find_element_by_id('search-key')
    searchFiled.send_keys(query)
    searchFiled.send_keys(Keys.RETURN)

    freeShipping = driver.find_element_by_xpath('//*[@id="linkFreeShip"]/i')
    freeShipping.click()

    minPrice = driver.find_element_by_xpath('//*[@id="filter-price-from"]')
    minPrice.send_keys("1000")
    maxPrice = driver.find_element_by_xpath('//*[@id="filter-price-to"]')
    maxPrice.send_keys("2000")
    maxPrice.send_keys(Keys.RETURN)

    sortField = driver.find_element_by_xpath('//*[@id="sortBySelect"]/div')
    sortField.click()
    sortHighPriceFirst = driver.find_element_by_xpath('//*[@id="sortBySelect"]/ul/li[5]/a')
    sortHighPriceFirst.click()

except Exception as ex:
    logException("AliExpress Test", __file__, ex)
    driver.quit()

