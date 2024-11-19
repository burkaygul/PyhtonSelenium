from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\Burkay9\PycharmProjects\PythonTesting\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise")

country = driver.find_element(By.CSS_SELECTOR, "#autosuggest")
country.send_keys("ind")
sleep(2)

countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
print(len(countries))

for eachCountry in countries:
    if eachCountry.text == "India":
        eachCountry.click()
        break



#print(country.text)
assert country.get_attribute("value") == "India"