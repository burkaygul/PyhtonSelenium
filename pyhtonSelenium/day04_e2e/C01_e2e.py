from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Users\Burkay9\PycharmProjects\PythonTesting\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# xpath //a[contains(@href,'shop')]
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()

shop_items = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for eachShopItem in shop_items:
    productName = eachShopItem.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        eachShopItem.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='primary']").click()

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys("tur")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Turkey")))
driver.find_element(By.LINK_TEXT, "Turkey").click()

driver.find_element(By.CSS_SELECTOR,"div[class='checkbox checkbox-primary']").click()

driver.find_element(By.XPATH, "//*[@type='submit']").click()

actualText = driver.find_element(By.CLASS_NAME, "alert-success").text
expectedText = "Success!"

assert  expectedText in actualText