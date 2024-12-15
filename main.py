from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.saucedemo.com/')

user_message = driver.find_element(By.ID, "user-name")
user_message.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
sleep(5)
