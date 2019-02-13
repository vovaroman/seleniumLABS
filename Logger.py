from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from Driver import *

def  logException(caseName,fileName, error):
    print("File Name: " + str(fileName) + "\nCase name:" + caseName + "\nException: " + str(error))
    

