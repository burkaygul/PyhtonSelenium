from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice")

# ID, Xpath, CSSSelector, Classname, name, LinkText

# CSS tagname[attribute='value'], #id, .classname
driver.find_element(By.CSS_SELECTOR,"div>input[name='name']").send_keys("burkaygul")
sleep(2)
driver.find_element(By.NAME, "email").send_keys("burkaygul96@gmail.com")
sleep(2)
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Burkay9")
sleep(2)
driver.find_element(By.ID,"exampleCheck1").click()
sleep(2)

genderElement = driver.find_element(By.ID,"exampleFormControlSelect1")
select = Select(genderElement)

select.select_by_visible_text("Female")
sleep(2)
driver.find_element(By.ID,"inlineRadio1").click()
sleep(2)
driver.find_element(By.NAME, "bday").send_keys("24081996")

# XPath ---- //tagname[@attribute='value']
driver.find_element(By.XPATH,"//input[@value='Submit']").click()


sleep(5)
message = driver.find_element(By.XPATH, "//strong").text
print(message)

assert "Success" in message