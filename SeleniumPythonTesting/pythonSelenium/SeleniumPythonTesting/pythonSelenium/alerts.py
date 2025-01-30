import time

from selenium import webdriver
from selenium.webdriver.common.by import By

name = "Alok Kumar!"

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert1 = driver.switch_to.alert
alertText = alert1.text
print(alertText)

assert name in alertText #it will check if name is present in the alertText

alert1.accept() #helps us to click OK instead of dismiss
# alert1.dismiss()





time.sleep(3)