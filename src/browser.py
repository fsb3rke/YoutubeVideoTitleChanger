from selenium import webdriver
import time
import pref

with open('pref.json') as f:
    data = json.load(f)

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
        #youtube acc mail
        signinMailInput.send_keys(pref.username)
        taym(2)
        contBtn = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
        taym(2)
        contBtn.click()
        taym(2)
        passwordInput = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        taym(2)
        passwordInput.click()
        taym(2)
        #youtube acc password
        passwordInput.send_keys("")
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
        taym(2)
        gotoMyvideo = self.browser.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[2]")
        taym(2)
        gotoMyvideo.click()
        taym(2)
        #chose your video
        self.browser.get("")
        taym(2)
        editvideoBtn = self.browser.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[9]/div[2]/ytd-video-secondary-info-renderer/div/div/div/ytd-button-renderer/a")
        taym(2)
        editvideoBtn.click()
        taym(2)
        analticBtn = self.browser.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/div/ytcp-navigation-drawer/nav/ytcp-animatable[2]/ul/li[2]/ytcp-ve/a/tp-yt-paper-icon-item")
        taym(2)
        analticBtn.click()
        taym(2)
        allViews = self.browser.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[13]/yta-app/yta-overview-app/div/yta-screen/div/ytcp-ve/div/div/yta-section[2]/yta-key-metric-card/yta-card-container/tp-yt-paper-card/div[2]/tp-yt-paper-listbox/tp-yt-paper-item[1]/yta-key-metric-block/div/span[1]/div[2]/div/div").text
        taym(2)
        print(allViews)
        taym(2)
        editBtn = self.browser.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/div/ytcp-navigation-drawer/nav/ytcp-animatable[2]/ul/li[1]/ytcp-ve/a")
        taym(2)
        editBtn.click()
        taym(2)
        videoTitle = self.browser.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-mention-textbox/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div")
        taym(2)
        videoTitle.clear()
        taym(2)
        videoTitle.send_keys(f"Bu videonun toplam görüntülenme sayısı: {allViews}")
        taym(2)
        saveBtn = self.browser.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-sticky-header/ytcp-entity-page-header/div/div[2]/ytcp-button[2]")
        taym(2)
        saveBtn.click()
        taym(2)
        goVideo = self.browser.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-details-section/ytcp-video-metadata-editor/ytcp-video-metadata-editor-sidepanel/ytcp-video-info/div/div[1]/div[1]/div[2]/span/a")
        taym(2)
        goVideo.click()
        taym(2)
