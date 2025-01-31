import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

email = ""
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
windowOpened = driver.window_handles

driver.switch_to.window(windowOpened[1])
sentence = driver.find_element(By.XPATH, "//div[@class='col-md-8']/p[2]").text

# email = sentence.split(" at ")[1].split(" ")[0]
# print("Extracted Email:", email)

# Regular expression to match email
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Extract email
match = re.search(email_pattern, sentence)
if match:
    email = match.group()
    print("Extracted Email:", email)
else:
    print("No email found.")

driver.close()

driver.switch_to.window(windowOpened[0])
time.sleep(2)
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("alok123")
buttonsRadio = driver.find_elements(By.CSS_SELECTOR, ".customradio")

buttonsRadio[1].click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR, "#terms").click()
driver.find_element(By.ID, "signInBtn").click()
# time.sleep(2)
# error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger col-md-12']").text
# print(error_message)

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

