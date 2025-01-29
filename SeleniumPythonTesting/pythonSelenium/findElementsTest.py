import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# print(driver.find_element(By.ID, "autosuggest").text) #it will not retrive the value because lists are loaded for the first time when application loaded.
print(driver.find_element(By.ID, "autosuggest").get_attribute("value")) #this is a javaScript DOM case
#So that means there is an attribute called value set in the backend and HTML code, so that the value will get updated whenever we enter something new in any edit box.

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"










time.sleep(3)
