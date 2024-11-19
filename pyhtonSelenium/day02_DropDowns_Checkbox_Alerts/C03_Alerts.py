from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\Burkay9\PycharmProjects\PythonTesting\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = "Burkay"

driver.find_element(By.ID, "name").send_keys(name)

driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

alert = driver.switch_to.alert

print(alert.text)
assert name in alert.text

alert.accept()
#alert.dismiss()