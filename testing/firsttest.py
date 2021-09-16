from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org")
print(driver.title)
search_bar = driver.find_element_by_name("q") #name attribute
search_bar.clear() # clear contents 
search_bar.send_keys("getting started with python") #type
search_bar.send_keys(Keys.RETURN) # enter
print(driver.current_url)
driver.close()
