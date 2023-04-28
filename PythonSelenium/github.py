from githubUserInfo import *
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By

class Github :
    def __init__(self,username,password) :
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
    def signIn(self):
        self.browser.get("https://github.com/login") 
        time.sleep(2)

        username = self.browser.find_element(By.XPATH,"//*[@id='login_field']")
        username.send_keys(self.username)
        password = self.browser.find_element(By.XPATH,"//*[@id='password']")
        password.send_keys(self.password)
        sign_in = self.browser.find_element(By.XPATH,"//*[@value='Sign in']")
        sign_in.click
    def getFollowers(self):
        self.browser.get("https://github.com/hanifehazirlar?tab=followers")
github = Github(username,password)
github.signIn()
time.sleep(1000)
        