from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\Burkay9\PycharmProjects\PythonTesting\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on column header
# collect all veggie names -> BrowserSortedveggieList
# sort this browserSortedveggieList => newSortedList
#browserSortedveggieList == newSortedList

driver.find_element(By.CSS_SELECTOR, "span[class='sort-icon sort-descending']").click()

veggieWebElements = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")

browserSortedVeggies = []
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

newSortedList = browserSortedVeggies.copy()


assert browserSortedVeggies == newSortedList