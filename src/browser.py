from selenium import webdriver
import time

def taym(taymc):
    time.sleep(taymc)

class Browser:
    def __init__(self, link):
        self.link = link
        self.browser = webdriver.Chrome()
        Browser.OpenBrowser(self)

    def OpenBrowser(self):
        self.browser.get(self.link)
        taym(2)
        Browser.Login(self)

    def Login(self):
        loginBtn = self.browser.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a")
        taym(2)
        loginBtn.click()
        taym(2)
        signinMailInput = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
        taym(2)
        signinMailInput.click()
        taym(2)
        signinMailInput.send_keys("berkedenemee@gmail.com")
        taym(2)
        contBtn = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
        taym(2)
        contBtn.click()
        taym(2)
        passwordInput = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        taym(2)
        passwordInput.click()
        taym(2)
        passwordInput.send_keys("Berke0595")
        taym(2)
        cont2Btn = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
        taym(2)
        cont2Btn.click()
        taym(2)
        hasPopup = self.browser.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-topbar-menu-button-renderer[3]/button")
        taym(2)
        hasPopup.click()
        taym(2)
        gotoMychannel = self.browser.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[1]/a")
        taym(2)
        gotoMychannel.click()
