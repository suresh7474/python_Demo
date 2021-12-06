from selenium import  webdriver

import os
chrome_intance=os.getcwd()+"\\Driver\\chromedriver.exe"
#use for launch chrome browser and hit the website
Web_url="https://opensource-demo.orangehrmlive.com/"
chrdriver=webdriver.Chrome(chrome_intance)
chrdriver.get(Web_url)
chrdriver.maximize_window()
print("open chrom")

#application fill informatin point to exact location
username=chrdriver.find_element_by_id("txtUsername")
password=chrdriver.find_element_by_id("txtPassword")
submitt=chrdriver.find_element_by_id("btnLogin")

username.send_keys("Admin")
password.send_keys("admin123")
submitt.click()

