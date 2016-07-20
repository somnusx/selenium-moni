from selenium import webdriver  
import time  
import os  
  

option = webdriver.ChromeOptions()
option.add_argument(r'--user-data-dir=C:\Users\somnus\AppData\Local\Google\Chrome\User Data\Default') #设置成用户自己的数据目录
browser = webdriver.Chrome(chrome_options=option)


browser.get('http://www.imooc.com/video/11346')

##browser.get('http://www.imooc.com/user/newlogin/')
##
##
##browser.find_element_by_xpath("//input[@name='email']").send_keys("13255290027")
##
##browser.find_element_by_xpath("//input[@name='password']").send_keys("132csvcsxcs156")
##
##browser.find_element_by_xpath("//input[@value='登录']").click()
##
##browser.find_element_by_xpath("//div[@id='login-area']/ul/li[3]/a/i").click()


