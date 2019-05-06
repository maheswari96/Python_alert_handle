# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:07:52 2019

@author: Harikrishna
"""
import time as t1
from selenium import webdriver
#driver=webdriver.Firefox()
driver=webdriver.Chrome()
driver.get("https://www.google.com/intl/en-GB/gmail/about/")
window=driver.window_handles[0]
print(window)
driver.find_element_by_xpath("//a[contains(text(), 'Sign in')]/parent::li/parent::ul/parent::div/parent::div/parent::div/following-sibling::div/div/div[5]/ul/li[3]/a").click()
t1.sleep(10)
window_1=driver.window_handles[1]
print(window_1)
driver.switch_to_window(window_1)
t1.sleep(10)
driver.find_element_by_name("firstName").send_keys("maheswari") 
driver.save_screenshot("text.png")
#driver.close()
#driver.quit()