from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path= './geckodriver')

try:
	links = [
	'https://twitter.com/login',
	'https://github.com/akshajdevkv/shortlink-maker',
	'https://selenium-python.readthedocs.io/locating-elements.html'
	]

	for link in links:
		driver.get('https://bitly.com/')
		url_input = driver.find_element_by_id('shorten_url')
		url_input.send_keys(link)
		driver.find_element_by_id('shorten_btn').click()
		time.sleep(3)
		#stores the shortened URL 
		shortlink = driver.find_element_by_css_selector('.short-link > a:nth-child(1)').text
		print('Original Link = '+link)
		print('Shortened Link = '+shortlink+'\n')
	

except Exception as e:
	print(e)
	#closes the browser
	driver.quit()