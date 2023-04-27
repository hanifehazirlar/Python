from selenium import webdriver
import time
driver = webdriver.Chrome()
url="https://amazon.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("Screenshut/amazon.com_homepage.png") # bulundugumuz ekranin ekran goruntusunu aldi

url = "http://kitapyurdu.com"
driver.get(url) # kitapyurdu sayfasina gitti

print(driver.title)

if "Kitapyurdu" in driver.title:
    driver.save_screenshot("Screenshut/Kitapyurdu.png")

time.sleep(2)
driver.back()
# driver.forward() sayfayi ileri
driver.close()