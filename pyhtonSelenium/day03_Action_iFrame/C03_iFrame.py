from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\Burkay9\PycharmProjects\PythonTesting\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(2)
driver.maximize_window()

driver.get("https://demoqa.com/frames")

driver.switch_to.frame("frame1")

print(driver.find_element(By.ID, "sampleHeading").text)
driver.switch_to.default_content()


sleep(5)