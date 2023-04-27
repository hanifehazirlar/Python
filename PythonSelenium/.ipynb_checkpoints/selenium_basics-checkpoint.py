from selenium import webdriver
import time
driver = webdriver.Chrome()
url="https://amazon.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("amazon.com_homepage.png")
print(driver.title)

time.sleep()
driver.close()