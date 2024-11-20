from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\Burkay9\PycharmProjects\PythonTesting\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")

CurrentWindowHandle = driver.current_window_handle


driver.find_element(By.LINK_TEXT, "Click Here").click()

windowHandles = driver.window_handles

for eachWindowHandle in windowHandles:
    if eachWindowHandle != CurrentWindowHandle:
        newWindow = eachWindowHandle

driver.switch_to.window(newWindow)

actualTitle = driver.title
print(actualTitle)
expectedTitle = "New Window"

assert expectedTitle == actualTitle

