#There are two types of wait, implicit and explicit,
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5) #implicit wait is more like global timeout on top of our script, we will declare a global timeout
#What it does -> if any element is not shown on the page, it will wait a max of "n" seconds for that to show up.

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div") #list[] will not be caught by an implicit wait. Selenium only checks whether a list is returned, not whether the list contains elements. Since an empty list is still a valid return, Selenium does not wait for elements to appear.
count = len(results)
print(count)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)



