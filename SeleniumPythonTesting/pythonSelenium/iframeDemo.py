from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demo.automationtesting.in/Frames.html")

driver.switch_to.frame("singleframe")

driver.find_element(By.XPATH, "//input[@type='text']").clear()
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("I am able to enter the text")


driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h1").text)

