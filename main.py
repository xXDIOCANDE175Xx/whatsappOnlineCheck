from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# XPath selectors
NEW_CHAT_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]'
INPUT_TXT_BOX = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/label[1]/div[1]/div[2]'
ONLINE_STATUS_LABEL = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[2]/span[1]"

# Replace below with the list of targets to be tracked
TARGETS = {'"name"': 'number_international_format'}

# Replace below path with the absolute path
browser = webdriver.Chrome(r'/path/to/file')

# Load Whatsapp Web page
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)

while True:
    os.system('clear')
    for target in TARGETS:
        tryAgain = True
        new_chat_title = wait.until(EC.presence_of_element_located((By.XPATH, NEW_CHAT_BTN)))
        while (tryAgain):
            try:
                new_chat_title.click()
                input_box = wait.until(EC.presence_of_element_located((By.XPATH, INPUT_TXT_BOX)))
                time.sleep(0.5)
                input_box.send_keys(TARGETS[target])
                time.sleep(1)
                input_box.send_keys(Keys.ENTER)
                time.sleep(5)
                tryAgain = False
                try:
                    try:
                        named_tuple = time.localtime() # get struct_time
                        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
                        f=open("output.log","a")
                        browser.find_element_by_xpath(ONLINE_STATUS_LABEL)
                        f.write(time_string+"--- "+target+" ---Online\n")
                        print(target + ' is online')
                        time.sleep(1)
                        f.close()
                    except:
                        print(target + ' is offline')
                    time.sleep(1)
                except:
                    print('Exception 1')
                    time.sleep(10)
            except:
                print('Exception 2')
                time.sleep(4)
