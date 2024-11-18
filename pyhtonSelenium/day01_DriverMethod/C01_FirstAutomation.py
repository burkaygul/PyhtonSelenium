import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome driver service Selenium 160 -> 160 chrome driver
#service_obj = Service(r"C:\Users\Burkay9\PycharmProjects\PythonTesting\chromedriver.exe")
#driver = webdriver.Chrome(service = service_obj)
"""
in Java;
System.setProperty("webdriver.chrome.driver","setupFiles/chromedriver.exe");

"""



driver = webdriver.Edge()
driver.get("https://www.amazon.de")
driver.maximize_window()
print(driver.current_url)


time.sleep(2)
