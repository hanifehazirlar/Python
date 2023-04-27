import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
url = "http://github.com"
driver.get(url)

search_input = driver.find_element(By.NAME,"q")
time.sleep(1)
search_input.send_keys("python")
time.sleep(3)
search_input.send_keys(Keys.ENTER)
time.sleep(2)
result = driver.find_elements(By.CSS_SELECTOR, '.f4.text-normal')
for element in result :
   print(element.text)

# result = driver.page_source   # yukaridaki kod yazimi yerine bu sekilde de kisayoldan bulabiliriz

    
#driver.close()