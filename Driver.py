from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

def install_driver():
    dirname = os.getcwd()
    return webdriver.Chrome(dirname + "/chromedriver")
