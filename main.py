from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime
import getpass
import sys

class Instabot:
    def __init__(self, username, pw):
        #self.options = Options()
        #self.options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(ChromeDriverManager().install())#, options=self.options)
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(4)
    
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(5)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/followers/')]".format(self.username))\
            .click()
        sleep(1)
        followers = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/following/')]".format(self.username))\
            .click()
        sleep(1)
        following = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print('>> This is a list of people who do not follow you back:\n')
        print(*not_following_back, sep='\n')
        print('\n\n')

    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        sleep(4)
        while last_ht != ht:
            last_ht = ht
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
            sleep(3)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text!='']
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button')\
            .click()
        return(names)
    
    def exit(self):
        self.driver.quit()

#printing start
print('Initiating process....')
print('Date and time of starting: '+str(datetime.today()))
print('\n\n')
print(r'''8888888                   888                                                                       
  888                     888                                                                       
  888                     888                                                                       
  888   88888b.  .d8888b  888888  8888b.   .d88b.  888d888 8888b.  88888b.d88b.                     
  888   888 "88b 88K      888        "88b d88P"88b 888P"      "88b 888 "888 "88b                    
  888   888  888 "Y8888b. 888    .d888888 888  888 888    .d888888 888  888  888                    
  888   888  888      X88 Y88b.  888  888 Y88b 888 888    888  888 888  888  888                    
8888888 888  888  88888P'  "Y888 "Y888888  "Y88888 888    "Y888888 888  888  888                    
                                               888                                                  
                                          Y8b d88P                                                  
                                           "Y88P"                                                   
888     888                  .d888         888 888                                                  
888     888                 d88P"          888 888                                                  
888     888                 888            888 888                                                  
888     888 88888b.         888888 .d88b.  888 888  .d88b.  888  888  888  .d88b.  888d888 .d8888b  
888     888 888 "88b        888   d88""88b 888 888 d88""88b 888  888  888 d8P  Y8b 888P"   88K      
888     888 888  888 888888 888   888  888 888 888 888  888 888  888  888 88888888 888     "Y8888b. 
Y88b. .d88P 888  888        888   Y88..88P 888 888 Y88..88P Y88b 888 d88P Y8b.     888          X88 
 "Y88888P"  888  888        888    "Y88P"  888 888  "Y88P"   "Y8888888P"   "Y8888  888      88888P' 
                                                                                                    ''')
print("\n>> This is an app I created which will just simply tell you about people you follow on Instagram who don't follow you back.")
print('''>> You can clearly see the process as the program runs by itself, which should take less than 5 minutes according to your internet connection.''')
print('''>> It doesn't require heavy amount of internet but time may vary according to speed.\n\n''')
print('>> To terminate the program at any time, just press ([Ctrl] + [C])')
print('>> During the process, please do NOT click on the browser as it may disrupt the program.')
print(">> Just let the program run on it and it will show result")
while True:
    username = input('\nPlease enter your exact instagram username -\n')
    if len(username)<1:
        print('Error: please enter your correct username')
    else:
        break
while True:
    pw = getpass.getpass('\nPlease enter your password -\n')
    if len(pw)<1:
        print('Error: please enter your password')
    else:
        break
print('\nInstalling webdriver. Please wait as this may take time according to your internet connection.\n\n')
try:
    my_bot = Instabot(username, pw)
    my_bot.get_unfollowers()
    my_bot.exit()
except:
    print('>> Some error detected, could be caused due to slow internet speed, please kindly restart process, sorry for the inconvenience!')
    try:
        my_bot.exit()
    except:
        pass
    sleep(2)
    sys.exit()