from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def write_csv(data):
    with open ("instagram.csv",'a') as file:
        writer = csv.writer(file)
        writer.writerow( [ data['handle'], data['posts'], data['followers'], data["following"] ] )

def Login():
    PATH = "chromedriver_linux64/chromedriver"
    
    global browser
    browser = webdriver.ChromeOptions() #Chromedriver path.
    browser.add_argument("start-maximized");
    browser.add_argument("disable-infobars")
    browser.add_argument("--disable-extensions")
    browser = webdriver.Chrome(chrome_options=browser, executable_path=PATH) # <----- ENTER PATH HERE
    
    browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher') #website you require to automate and run
    time.sleep(2)

    nameList = []
    username = browser.find_element_by_name('username')
    username.send_keys(#ENTER USERNAME)
    password = browser.find_element_by_name('password')
    password.send_keys(#ENTER PASSWORD)
    nextButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button")
    nextButton.click()
    time.sleep(4)
    
    notifbutton = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    notifbutton.click()

import csv
nameList = []
with open ("nameList.csv",'r') as file:
    for name in file:
        nameList.append(name)

Login()
FinalList = []
for name in nameList:
    browser.get("https://www.instagram.com/"+name)
    time.sleep(2)
    items = browser.find_elements_by_tag_name("li")
    for item in items:
        text = [item.text]
        if text != [""]:
            if "posts" in text[0]:
                posts = text[0]
            elif "followers" in text[0]:
                followers = text[0]
            elif "following" in text[0]:
                following = text[0]
    entries = {"handle":name,"posts":posts,"followers":followers,"following":following}
    print(entries)
    FinalList.append(entries)

for entry in FinalList:
    write_csv(entry)
