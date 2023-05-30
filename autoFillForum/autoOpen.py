from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import requests

chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
url = 'http://ecmp.baosight.com:9080/ecmp/login.jsp'
driver.get('http://ecmp.baosight.com:9080/ecmp/login.jsp')

# driver.add_cookie({'name':'JSESSIONID', 'value':'0000kIl2auCkwyrJxBsyHtxpHG7:-1'})
username = driver.find_element(By.ID, "p_username")
password = driver.find_element(By.ID, "p_password")
captcha = driver.find_element(By.ID, "p_captcha")
imgUrl = driver.find_element(By.CLASS_NAME, "identifyingcodeImg").get_attribute('src')
# print(imgUrl)

username.send_keys("173941")
password.send_keys("2kxEn4RD@Jxk")
captcha.send_keys()
r = requests.get(imgUrl)

with open('1.jpg','wb') as f:
    f.write(r.content)

# driver.find_element(By.ID, "kw").send_keys("https://blog.csdn.net/qq_19309473")
# driver.find_element(By.ID, "su").click()
# ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(
#     Keys.CONTROL).perform()
