from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# create a webdriver object
wd = webdriver.Chrome()

# navigate to a web page
wd.get("http://35.178.198.206/index.html")

# navigate to page with credit card details
time.sleep(5)
l = wd.find_element(By.PARTIAL_LINK_TEXT, "Enter credit card details")
l.click()

# fill in the fields on the form
time.sleep(2)
f = wd.find_element(By.NAME, "cardholder")
f.send_keys("smith john")

time.sleep(2)
f = wd.find_element(By.NAME, "cardnumber")
f.send_keys("1223")

time.sleep(2)
f.submit()

# navigate back to the home page again
time.sleep(2)
l = wd.find_element(By.PARTIAL_LINK_TEXT, "Go back to index")
l.click()

time.sleep(3)
l = wd.find_element(By.PARTIAL_LINK_TEXT, "Retrieve credit")
l.click()

time.sleep(2)
f = wd.find_element(By.NAME, "cardholder")
f.send_keys("smith john")

time.sleep(2)
f.submit()

time.sleep(2)
l = wd.find_element(By.PARTIAL_LINK_TEXT, "Go back to index")
l.click()

# close the browser
time.sleep(5)
wd.quit()