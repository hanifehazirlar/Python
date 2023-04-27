# once terminale pip install selenium yazip selenium kutuphanesini yukledik
from selenium import webdriver # selenium kutuphanesinden webdriver modulunu cagirdik
driver = webdriver.Chrome()
url = "https://amazon.com"
driver.get(url)