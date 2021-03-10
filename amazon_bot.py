from selenium import webdriver
import webdriver_manager.chrome
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from auth import email, password, uri
from pynput.keyboard import Key, Controller

#the sleeps are needed to make sure all elemnts of the site are loaded just fine

class BrowserBot:
    def __init__(self):
        # Create a browser we can play on
        self.Browser = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())

    def log_on(self):
        """First, we must log into our Amazon account"""
        self.Browser.get(uri)
        sleep(2)
        self.Browser.find_element_by_xpath('//*[@id="nav-link-accountList"]').click()
        sleep(2)
        self.Browser.find_element_by_xpath('//*[@id="ap_email"]').send_keys(email + Keys.RETURN)
        sleep(2)
        self.Browser.find_element_by_xpath('//*[@id="ap_password"]').send_keys(password + Keys.RETURN)



print('Please acknowledge, that you - the person using this script - are taking full responsibility for using this script and all trouble that might come from it')
response = input('Type "I acknowledge" and press Return :> ')
if (response != 'I acknowledge') :
  exit()
print('OK')  
# Call the self
zonie = BrowserBot()
zonie.log_on()
## let user input otp token if required and wait for input at commandline
input() 
not_done = True
while not_done :
    try:
        ## i highly recommend trying with an available product, modifying the xpaths to any values of available items. you can easily find the xpath in firefox's firebug - just 
        ## ctrl+shift+c, select the element, and in the plaintext view right-click->copy->xpath

        #open product url
        zonie.Browser.get('https://www.amazon.de/Sony-Interactive-Entertainment-PlayStation-5/dp/B08H93ZRK9/ref=sr_1_2?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=playstation%2B5&qid=1615301139&sr=8-2&th=1')
        #choose "subproduct - ie ps5"
        zonie.Browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[5]/div[4]/div[29]/div[1]/div/form/div/ul/li[6]/span/div/span/span/span/button').click()
        sleep(3)
        zonie.Browser.find_element_by_xpath('//*[@id="add-to-cart-button"]').click()
        not_done=False
    except:
        not_done=True
sleep(3)
zonie.Browser.get('https://www.amazon.de/gp/cart/view.html?ref_=nav_cart')
sleep(3)
zonie.Browser.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div[3]/div/div[1]/div[2]/div/form/div/div/span/span/input').click()
sleep(3)
####
## it was all fun and games up to this point. uncomment the next line, only if you are sure you trust the shopping process so far.
##
## zonie.Browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/span/span/input').click()
####

## keep order complete page open until input at commandline
input()
