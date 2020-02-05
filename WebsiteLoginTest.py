from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import mytools
import csv
import bs4
import sys







usernameStr = "XXX"
passwordStr = "XXX"
baseurl = 'http://XXXX'

Login():
    driver = webdriver.Chrome("/Users/XXXXX/Downloads/chromedriver")
    driver.get(('http://XXXXX'))
    username = driver.find_element_by_id('user_username')
    username.send_keys(usernameStr)
    password = driver.find_element_by_id('user_password')
    password.send_keys(passwordStr)

    signInButton = driver.find_element_by_xpath('//*[@id="user_new"]/div[4]/input')
    signInButton.click()




