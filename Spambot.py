from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from selenium.webdriver.chrome.options import Options
from getpass import getpass
import time
import random

opt = Options()
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
    })

def path():
    global mah
    # starts a new chrome session
    mah = webdriver.Chrome(r"E:\WebDrivers\chromedriver.exe",options=opt,service_log_path='NUL') # Add path if required

def codychat():
    username = input("Enter in your username: ")
    password = getpass("Enter your password: ")
    inputString = input("Enter message to send: ")
    url = input("Enter the website to spam: ")

    path()

    mah.get(url)
    time.sleep(5)
    enter = mah.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div[2]/button[1]")     
    enter.click()
    time.sleep(2)
    username_textbox = mah.find_element_by_id("user_username")
    username_textbox.send_keys(username)

    password_textbox = mah.find_element_by_id("user_password")
    password_textbox.send_keys(password)

    login = mah.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div[2]/button")     
    login.click()

    time.sleep(3)

    see = mah.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div[4]/div[2]/div/div[1]")
    see.click()

    time.sleep(10)

    i=0
    while i<= 1:
        sendmsg = mah.find_element_by_name("content")
        sendmsg.send_keys(inputString)
        submit = mah.find_element_by_id("submit_button")
        submit.click()
        time.sleep(3)

def insta():
    username = input('Enter your Username:  ')
    password = getpass("Enter your password: ")
    inputString = input("Enter message to send: ")
    url = 'https://instagram.com/' +input('Enter username of user whom you want to send message: ')
    path()
    mah.get("https://www.instagram.com/accounts/login/")

    time.sleep(4)
    usern = mah.find_element_by_name("username")
	
    # sends the entered username
    usern.send_keys(username)

    # finds the password box
    passw = mah.find_element_by_name("password")

    # sends the entered password
    passw.send_keys(password)
	
    # press enter after sending password
    passw.send_keys(Keys.RETURN)
    time.sleep(5.5)

    mah.get(url)
    time.sleep(4)

    message = mah.find_element_by_class_name('_862NM ')
    message.click()
    time.sleep(4)
    mah.find_element_by_class_name('HoLwm ').click()
    time.sleep(1)

    i=0
    while i<= 1:
        sendmsg = mah.find_element_by_tag_name('textarea')
        sendmsg.send_keys(inputString)
        sendmsg.send_keys(Keys.RETURN)
        time.sleep(1)

def fb():
    username = input("Enter in your username: ")
    password = getpass("Enter your password: ")
    friend = input("Enter your friend name to message: ")
    message = input("Enter your message to your friend: ")
    
    path()
    mah.implicitly_wait(15)

    mah.get('https://www.facebook.com/')
    username_textbox = mah.find_element_by_name("email")
    username_textbox.send_keys(username)

    password_textbox = mah.find_element_by_name("pass")
    password_textbox.send_keys(password)

    time.sleep(2)

    login = mah.find_element_by_name("login")     
    login.click()
    time.sleep(5)

    msg = mah.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/span/div/div[1]")
    msg.click()
    time.sleep(3)

    search = mah.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/div/label/input')
    search.send_keys(friend)
    time.sleep(4)

    select = mah.find_element_by_xpath("//*[@id='112000183529612']/div/a/div")
    select.click()
    
    i=0
    while i<= 1:

      enter = mah.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]")
      enter.send_keys(message)

      send = mah.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/span[2]/div")
      send.click()

if __name__=="__main__":
    
	op = int(input(("1. CodyChat\n2. Instagram\n3. Facebook\nEnter option : ")))
	
	if(op==1):
		codychat()
	if(op==2):
		insta()
	if(op==3):
		fb()    
