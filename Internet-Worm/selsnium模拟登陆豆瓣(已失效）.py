from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.douban.com")

time.sleep(3)
# driver.find_element_by_class_name("account-tab-account on").click()
driver.find_element_by_id("username").send_keys("georgel.supertramp@gmail.com")
driver.find_element_by_id("password").send_keys("liqiaozhi1994")
driver.find_element_by_class_name("btn btn-account btn-active").click()


cookies = driver.get_cookies()
cookies_requests = {i["name"]:i["value"] for i in cookies}
print(cookies_requests)