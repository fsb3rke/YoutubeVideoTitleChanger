from selenium import webdriver
import time

class Browser:
    def __init__(self, link):
        self.link = link
        self.browser = webdriver.Chrome()
        Browser.OpenBrowser(self)

    def OpenBrowser(self):
        self.browser.get(self.link)