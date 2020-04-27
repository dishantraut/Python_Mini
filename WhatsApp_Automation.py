""" Whatsapp Automation """

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.headless = False

path = "C:\\Users\\Dishant\\Desktop\\chromedriver\\chromedriver"
driver = webdriver.Chrome(executable_path = path , options = options)
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')

search_box = driver.find_element_by_class_name('_2zCfw')

search_box.click()

search_box.send_keys(name)
search_box.send_keys(Keys.RETURN)

msg = input('Enter your message : ')
count = int(input('Enter the count : '))

#input('Enter anything after scanning QR code')

msg_box = driver.find_element_by_class_name('_3u328')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
