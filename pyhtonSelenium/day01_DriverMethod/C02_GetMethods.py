from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj = Service(r"/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice")

print(driver.title)
print(driver.current_url)
print(driver.current_window_handle)
print(driver.window_handles)
print(driver.page_source)


sleep(5)


driver.quit()



