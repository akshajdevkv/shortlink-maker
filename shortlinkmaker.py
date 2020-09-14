from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path= 'your/driver/path',options=options)
class Short_Link_Maker:
	def __init__(self):
		None 
	def shorten(self,url):
		self.url = url
		try:
			link = self.url
			driver.get('https://bitly.com/')
			driver.implicitly_wait(10)
			url_input = driver.find_element_by_id('shorten_url')
			url_input.send_keys(link)
			driver.find_element_by_id('shorten_btn').click()
			driver.implicitly_wait(10)
			shortlink = driver.find_element_by_css_selector('.short-link > a:nth-child(1)').text
			print('Original Link = '+link)
			print('Shortened Link = '+shortlink+'\n')

		except Exception as e:
			print(e)

		driver.quit()