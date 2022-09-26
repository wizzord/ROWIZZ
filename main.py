# Created By wizz

import json
import selenium
import random
import string
import os
import time
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

print(f"[{Fore.RED}WIZZ{Fore.RESET}] {Fore.GREEN}Checking Configuration File")
with open('config.json','r') as f:
    try:
        load = json.loads(f.read())
        loopamt = load['amtOfAccounts']
        gender = load['gender']
        prefix = load['usernamePrefix']
        if gender not in [0,1,2]:
            print(f"[{Fore.RED}WIZZ{Fore.RESET}] {Fore.GREEN}Invalid Gender")
            exit(0)
    except Exception as e:
        print(f"[{Fore.RED}WIZZ{Fore.RESET}] {Fore.GREEN}Error in Configuration File")

delay = 60
chars = string.ascii_lowercase + string.digits

try:
    print(f"[{Fore.RED}WIZZ{Fore.RESET}] {Fore.GREEN}Starting Account Generation")
    driver = webdriver.Firefox()
    for i in range(loopamt):
        driver = webdriver.Firefox()
        driver.get('https://roblox.com')
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'cookie-banner-wrapper')))
        driver.execute_script("""var l = document.getElementsByClassName("cookie-banner-wrapper")[0];
                                l.parentNode.removeChild(l);""")

        Select(driver.find_element(By.ID, 'MonthDropdown')).select_by_visible_text("February")
        Select(driver.find_element(By.ID, 'DayDropdown')).select_by_visible_text("06")
        Select(driver.find_element(By.ID, 'YearDropdown')).select_by_visible_text("1991")

        username = f"{prefix}_{''.join(random.choice(string.ascii_uppercase) for i in range(5))}"
        password = ''.join(random.choice(chars) for i in range(16))

        driver.find_element(By.ID, 'signup-username').send_keys(username)
        driver.find_element(By.ID, 'signup-password').send_keys(password)

        if gender == 0:
            gender = random.randint(1,2)

        if gender == 1:
            driver.find_element(By.ID, 'MaleButton').click()
        elif gender == 2:
            driver.find_element(By.ID, 'FemaleButton').click()

        driver.find_element(By.ID, 'signup-button').click()
        driver.find_element(By.ID, 'signup-button').click()

        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'cookie-banner-wrapper')))
        print(f"[{Fore.RED}WIZZ{Fore.RESET}] {Fore.GREEN}Account {i+1} Created: {username}")
        f = open('gen.txt','a')
        f.write(f"WIZZ | {username} | {password} \n")
        f.close()
        driver.close()
except Exception as e:
    print(f"[{Fore.RED}WIZZ{Fore.RESET}] {Fore.GREEN}Unexpected Error Occured > {e}")
    driver.close()
    exit(0)
