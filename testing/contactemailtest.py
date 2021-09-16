from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from PIL import Image
import os, json
from selenium import webdriver

def testEmail(email_input, driver):
    name_input = driver.find_element_by_id('sender')
    name_input.send_keys("Morgan Iverson")

    email_input = driver.find_element_by_id('email')
    email_input.send_keys("miverson@emich.edu")

    selector = Select(driver.find_element_by_id('reason'))
    selector.select_by_value("Other")

    message = driver.find_element_by_id('message')
    message.send_keys("Test Message\nTest Message\nTest Message\nTest Message\n")

    submit_button = driver.find_element_by_id('send-form')
    submit_button.click()
    ss_name = 'contact_email_results_' + str(len([name for name in os.listdir('results') if os.path.isfile(name) and 'email' in name])) + '.png'

    driver.maximize_window()
    driver.save_screenshot(ss_name)
    screenshot = Image.open(ss_name)
    screenshot.show()

    # driver.execute_script('window.print()')


    # driver.close()


 