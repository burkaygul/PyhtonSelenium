from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#headless mode
chrome_options =  webdriver.ChromeOptions()
chrome_options.add_argument("headless")

service_obj = Service(r"C:\Users\Burkay9\PycharmProjects\PythonTesting\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj, options= chrome_options) # options added
driver.implicitly_wait(2)
driver.maximize_window()


driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#scroll
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(5)

target_element = driver.find_element(By.ID,"product")
driver.execute_script("arguments[0].scrollIntoView(true);", target_element)

driver.get_screenshot_as_file("screen.png")
