from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from Driver import *


driver = install_driver()
link = "https://ru.akinator.com/"

driver.get(link)

playButton = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[2]/div[2]/a/span")
playButton.click()

time.sleep(5)
try:
    questionField = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="game_content"]/div/div[3]/div[1]/div[2]/p'))
    )
except Exception as ex:
    driver.quit()

