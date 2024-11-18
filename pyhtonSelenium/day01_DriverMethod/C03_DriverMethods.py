import time
from datetime import timedelta
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice")

driver.fullscreen_window()
sleep(2)
driver.maximize_window()
sleep(2)
driver.minimize_window()

sleep(5)