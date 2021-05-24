from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time

with open('settings.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

address = input()
driver = webdriver.Chrome(r'./chromedriver') 
driver.get(str(address)) 
driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]").click()
time.sleep(1)
class_ = driver.find_elements_by_xpath(f"//div//span[contains(., '{jdata['class']}')]")
for i in class_:
    try:
        i.click()
    except Exception as e:
        print(e)
for i in range(0, 14):
    driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]").click()
time.sleep(1)
number_ = driver.find_elements_by_xpath(f"//div//span[contains(., '{jdata['number']}')]")
for i in number_:
    try:
        i.click()
    except Exception as e:
        print(e)
time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(jdata['name'])
driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(jdata['id'])
time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[3]/div[1]/div/div/span").click()
time.sleep(5)
driver.close()