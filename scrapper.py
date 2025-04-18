from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def Login():
    PATH = "chromedriver_linux64/chromedriver"

    browser = webdriver.ChromeOptions() #Chromedriver path.
    browser.add_argument("start-maximized");
    browser.add_argument("disable-infobars")
    browser.add_argument("--disable-extensions")
    browser = webdriver.Chrome(chrome_options=browser, executable_path=PATH) # <----- ENTER PATH HERE
    
    browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher') #website you require to automate and run
    time.sleep(2)

    username = browser.find_element_by_name('username')
    username.send_keys(#ENTER USERNAME)
    password = browser.find_element_by_name('password')
    password.send_keys(#ENTER PASSWORD)
    nextButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button")
    nextButton.click()
    time.sleep(4)
    
    notifbutton = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    notifbutton.click()
