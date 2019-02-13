from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
from Driver import *
from Logger import *
from PIL import Image as ImagePil
from io import BytesIO

from base64 import b64decode
from wand.image import Image
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import math

import pytesseract


def get_element_screenshot(element: WebElement) -> bytes:
    driver = element._parent
    ActionChains(driver).move_to_element(element).perform()  # focus
    src_base64 = driver.get_screenshot_as_base64()
    scr_png = b64decode(src_base64)
    scr_img = Image(blob=scr_png)

    x = element.location["x"] + 750
    y = element.location["y"] + 415
    w = element.size["width"]
    h = element.size["height"]
    scr_img.crop(
        left=math.floor(x),
        top=math.floor(y),
        width=math.ceil(w),
        height=math.ceil(h),
    )
    return scr_img.make_blob()

driver = install_driver()
try:
    link = "https://simpalsid.com/user/register?default_locale_code=&hide_news=false&hide_wallet=false&project_id=999a46c6-e6a6-11e1-a45f-28376188709b&region_code=md"
    driver.get(link)
    email = driver.find_element_by_name('email')
    email.send_keys('test@hydrogen.com')

    login = driver.find_element_by_name('login')
    login.send_keys('test') 

    password = driver.find_element_by_name('password')
    password.send_keys('test') 

    captchaField = driver.find_element_by_name('captcha')
    captchaImage = driver.find_element_by_xpath('//*[@id="popup-register-captcha-input"]')
    
    image = get_element_screenshot(captchaImage)
    im = ImagePil.open(BytesIO(image)) 
    text = pytesseract.image_to_string(im)
    captchaField.send_keys(text)

    finalButton = driver.find_element_by_xpath('/html/body/div/div/div[1]/form/footer/button')
    #finalButton.click()
except Exception as ex:
    logException("Simpals Test", __file__, ex)




