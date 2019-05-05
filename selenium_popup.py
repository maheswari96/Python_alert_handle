# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 18:14:15 2019

@author: Harikrishna
"""

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/delete_customer.php")
driver.find_element_by_name("submit").click()
alert=driver.switch_to.alert
print(alert.text)
alert.dismiss()
