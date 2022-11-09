import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Account
op_id = (open('id.txt', 'r')).readlines(0)[0]
op_pw = (open('password.txt', 'r')).readlines(0)[0]

# Chrome Driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(5)

# Login
driver.get('https://talk.op.gg/s/lol/all?sort=top')
driver.find_element(By.XPATH, '//*[@id="header"]/header/div[2]/div[1]/a').click()
driver.find_element(By.NAME, 'email').send_keys(op_id)
time.sleep(0.2)
driver.find_element(By.NAME, 'password').send_keys(op_pw)