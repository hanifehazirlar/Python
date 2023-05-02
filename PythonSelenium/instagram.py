import time
from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
    def sign_in(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        email = self.browser.find_element(
            By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        password = self.browser.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        time.sleep(3)
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        # self.browser.find_element(
        #     By.XPATH, '//*[@id="mount_0_0_8M"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
    def getFollowers(self):
        self.browser.get(f"https://instagram.com/{self.username}/followers")
        time.sleep(5)
        followerList = self.browser.find_elements(
            By.XPATH, "//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']")
        for i in followerList:
            print(f"https://instagram.com/{i.text}/")

        #followersLink = self.browser.find_element(
         #   By.XPATH, "//*[@id='mount_0_0_QM']/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
        #followersLink.click()
        self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog] ul").find_elements(By.CSS_SELECTOR,"li")
       # toplu yoruma almak ıcın ıstedıgın yerı sec ctrl+k+c
       # toplu yorumdan kaldırmak icin istedigin yeri sec ctrl+k+u
instagrm = Instagram(username, password)
instagrm.sign_in()
instagrm.getFollowers()
time.sleep(135)
