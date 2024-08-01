from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Edge()
driver.get('https://baidu.com/')
element  = driver.find_element(By.ID, 'kw')
element .send_keys('中南大学')
sleep(4)	#需进行sleep否侧浏览器会立马关闭，导致无法看见现象
driver.quit()



# <input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">