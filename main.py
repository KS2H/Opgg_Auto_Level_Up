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
driver.get('https://member.op.gg/?redirect_url=//www.op.gg/')
driver.find_element(By.NAME, 'email').send_keys(op_id)
time.sleep(0.1)
driver.find_element(By.NAME, 'password').send_keys(op_pw)
time.sleep(0.1)
driver.find_element(By.CSS_SELECTOR, '#root > div > div > div > div.member-card-layout__inner > div > form > button.member-button.login__btn').click()
time.sleep(1)


# Get Links
articles = []
for i in range(10):
	link = 'https://talk.op.gg/s/lol/all?page=' + str(i)
	driver.get(link)
	for element in driver.find_elements(By.CLASS_NAME, 'article-list-item__info'):
		if element.get_attribute('href') not in articles:
			articles.append(element.get_attribute('href'))
	print('Page ' + str(i) + ' Done !')

# Enter Articles
for count in range(len(articles) - 1):
	driver.get(articles[count])
	try:
		element_class = driver.find_element(By.XPATH, '//*[@id="postVote"]/div/button[1]/span[1]').get_attribute('class')
		if element_class == "article-vote__up-arrow":
			driver.find_element(By.XPATH, '//*[@id="postVote"]/div/button[1]').click()
		print('Article ' + str(count) + ' Done !')
	except:
		print('Article deleted')
		pass
	time.sleep(0.4)

# Close
driver.close()
print('Done !')