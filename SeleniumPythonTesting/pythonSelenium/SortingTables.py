from selenium import webdriver
from selenium.webdriver.common.by import By

BrowserSortedveggie = []
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

#collect all veggie names -> BrowserSortedveggieList
veggiWebElement = driver.find_elements(By.XPATH, "//tr/td[1]")
for eli in veggiWebElement:
    BrowserSortedveggie.append(eli.text)

originalBrowserSortedveggie = BrowserSortedveggie.copy()

#sort this BrowserSortedveggieList => newSortedList
BrowserSortedveggie.sort()

#BrowserSortedveggieList == newSortedList
assert BrowserSortedveggie == originalBrowserSortedveggie