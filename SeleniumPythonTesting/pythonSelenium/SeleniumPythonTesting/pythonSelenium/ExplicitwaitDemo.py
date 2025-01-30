import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
# An implicit wait tells Selenium to wait for a certain amount of time before throwing a NoSuchElementException if an element is not immediately available.
# It applies globally to all elements in the script.
# Once set, it remains valid for the entire WebDriver session.

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

#---------Sum validation-------
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
s = 0 #sum
for price in prices:
    s = s + int(price.text)

print(s)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert s == totalAmount



driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

#------Explicit wait-----------------
# An explicit wait waits for a specific condition to be met before proceeding.
# It is applied to individual elements rather than globally.
# More flexible than implicit waits since it allows waiting for conditions like visibility, clickability, etc.
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)









# Feature		    Implicit Wait				        Explicit Wait
# Scope		        Applies globally to all elements	Applies to specific elements
# Conditions	    Only checks element presence		Supports conditions like visibility, clickability, etc.
# Flexibility	    Less flexible				        More control over waiting conditions
# Performance	    May cause unexpected delays		    Optimized for specific cases



#---------------Why Not Use time.sleep()?------------------

# It adds unnecessary delay – Even if the element loads quickly, Selenium still waits for the full duration.
# It is not dynamic – It does not adjust based on the actual load time of the element.
# It reduces test efficiency – Slows down execution unnecessarily.
# It is not reliable – If network speed varies, time.sleep() might cause flaky tests