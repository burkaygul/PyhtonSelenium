import time
from time import sleep

import keyboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Users\Burkay9\PycharmProjects\PythonTesting\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div") #list []
count = len(results)

assert count > 0

for eachProduct in results:
    eachProduct.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
applyText = driver.find_element(By.CLASS_NAME, "promoInfo").text

print(applyText)