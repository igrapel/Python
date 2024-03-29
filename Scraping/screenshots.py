#Imports Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import os
#Opens up web driver and goes to Google Images
driver = webdriver.Chrome(executable_path=r'C:\Users\323917\OneDrive - Miami-Dade County Public Schools\Desktop\Portfolio\bin\chromedriver_win32\chromedriver.exe')
driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')

box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
country ="Italy Flag"
box.send_keys(country)
box.send_keys(Keys.ENTER)

#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

parent_dir = 'C:\\Users\\323917\\OneDrive - Miami-Dade County Public Schools\\Desktop\\Portfolio'
path = os.path.join(parent_dir, country)
os.mkdir(path)

for i in range(1, 200):
    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot(path + "\\flag(" + str(i) + ").png")
    except:
        pass

print(path)
