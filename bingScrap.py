import random
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import colorama
import sys
from selenium.webdriver.chrome.service import Service
from progress.bar import Bar
from colorama import Back, Fore, Style

def Banner():
    colorama.init(autoreset=True)
    print(Fore.RED + """                                                                      
 @@@@@@    @@@@@@@  @@@@@@@    @@@@@@   @@@@@@@   @@@@@@@@  @@@@@@@   
@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  
!@@       !@@       @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!  @@@  
!@!       !@!       !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!!@@!!    !@!       @!@!!@!   @!@!@!@!  @!@@!@!   @!!!:!    @!@!!@!   
 !!@!!!   !!!       !!@!@!    !!!@!!!!  !!@!!!    !!!!!:    !!@!@!    
     !:!  :!!       !!: :!!   !!:  !!!  !!:       !!:       !!: :!!   
    !:!   :!:       :!:  !:!  :!:  !:!  :!:       :!:       :!:  !:!  
:::: ::    ::: :::  ::   :::  ::   :::   ::        :: ::::  ::   :::  
:: : :     :: :: :   :   : :   :   : :   :        : :: ::    :   : :  
                                                     coded by KHASEY               
        """)

def Start(driver):
    try: driver.get("https://www.bing.com/")
    except: print("Problem with the custom header")  

def Wait():
    time.sleep(3)
        
def Search(driver, current):
    try:
        search_box = driver.find_element(By.XPATH,'//*[@id="sb_form_q"]')
        for char in current:
            search_box.send_keys(char)
            time.sleep(0.2)  # Attendez un bref moment entre chaque caractère
        
        Wait()
        driver.find_element(By.XPATH,'//*[@id="sb_form_q"]').send_keys(Keys.ENTER)
    except:
        print("pas de recherche")
  

def Write(driver):
    try:
        cites = driver.find_elements(By.TAG_NAME, 'cite')
        with open('websitegoogle.txt', 'a') as f:
            for cite in cites:
                if cite.text.startswith("http"):
                    f.write("%s\n" % cite.text)
    except:
        print("pas de file")

                
        

def Next(driver):
    try:
        count = 0
        while True:
            # if count == 200:
            #     break
            bar = Bar(Fore.RED + 'Pages =>', max=count, fill='#')
            ret_elements = driver.find_element(By.CSS_SELECTOR,'.sb_pagN')
            if ret_elements:  # Sélectionnez le second élément
                Write(driver)
                time.sleep(1)
                ret_elements.click()
                bar.next(count)
                count += 1 
            else:
                break        
            
    except:
        print(Fore.GREEN + "Scarp is over")

Banner()

if len(sys.argv) < 2:
    print("usage => python3 <prog name> <args>")
    exit()

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',  # Tor Browser for Windows and Linux
    'Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0',  # Tor Browser for Android
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
    
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
    
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '

    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
]

options = FirefoxOptions()
options.add_argument(f'user-agent={random.choice(user_agents)}')

driver = webdriver.Firefox(service=Service('./geckodriver'), options=options)
first = True
for current in sys.argv[1:]:
    print("Processing argument: " + current)
    Start(driver)
    Wait()
    Search(driver, current)
    Wait()
    Next(driver)
driver.quit()

