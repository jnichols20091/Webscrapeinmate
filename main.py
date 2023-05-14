from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests


options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("http://sheriff.jccal.org/NewWorld.InmateInquiry/AL0010000/")
driver.find_element(By.XPATH, "//input[@value='Search']").click()
name_elements = driver.find_elements(By.XPATH, "//*[@id='Inmate_Index']/div[2]/div[2]/table/tbody/tr/td")
for name in name_elements:
    name = name.text
    name = name.split('\n')
    if name == ['']:
        continue
    else:
        print(name)


# for name in name_elements:
#     print(name.text)
