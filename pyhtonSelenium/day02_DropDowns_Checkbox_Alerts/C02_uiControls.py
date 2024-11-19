from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\Burkay9\PycharmProjects\PythonTesting\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
print(len(checkboxes))

for eachCheckbox in checkboxes:
    if eachCheckbox.get_attribute("value") == "option2":
        eachCheckbox.click()
        sleep(2)
        assert eachCheckbox.is_selected()
        break

radioButtons = driver.find_elements(By.CSS_SELECTOR, "input[name='radioButton']")
print(len(radioButtons))

radioButtons[2].click()
assert radioButtons[2].is_selected()

assert driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()

driver.find_element(By.ID, "hide-textbox").click()

assert not driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()

