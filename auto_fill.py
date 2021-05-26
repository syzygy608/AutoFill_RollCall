from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time
import os

csfp = os.path.dirname(os.path.realpath(__file__))
json_file = os.path.join(csfp, "config.json")
with open(json_file, 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

print("新竹高中點名表自動填寫程式 by Syzygy0\n請記得至config.json更改裡面的資料為個人資料")
address = input("[請在此輸入點名表網址] : ")
driver = webdriver.Chrome(os.path.join(csfp, 'chromedriver')) 
driver.get(str(address)) 
time.sleep(2)

if (driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[2]/span")):
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[2]/span").click()
    time.sleep(1)
    driver.find_element_by_id("identifierId").send_keys(jdata["email"])
    time.sleep(1)
    driver.find_element_by_id("identifierNext").click()
    time.sleep(2)
    driver.find_element_by_name("password").send_keys(jdata["password"])
    time.sleep(1)
    driver.find_element_by_id("passwordNext").click()
    time.sleep(4)
else:
    time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]").click()
time.sleep(1)
class_ = driver.find_elements_by_xpath(f"//div//span[contains(., '{jdata['class']}')]")
for i in class_:
    try:
        i.click()
    except Exception as e:
        print(e)
time.sleep(1)
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
time.sleep(2)
driver.close()
