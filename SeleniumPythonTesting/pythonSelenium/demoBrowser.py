import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Chrome driver services
# service_obj = Service(r"C:\Users\Quicket-Solutions\Documents\chromedriver-win64.exe")
# driver = webdriver.chrome(service = service_obj)

#Edge driver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)













time.sleep(3)