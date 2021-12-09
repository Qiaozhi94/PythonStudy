from selenium import webdriver
import time



# selenium加载网页，即实例化一个网页
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# selenium的定位与操作
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()



# selenium获取html字符串
print(driver.page_source)  # 浏览器中的element的内容
print(driver.current_url)  # 获取当前网页的url地址

# 获取requests库可以直接使用的cookies
cookie = driver.get_cookies()
print(cookie)
cookies_requests = {i["name"]:i["value"] for i in cookie}
print(cookies_requests)
time.sleep(1)

# selenium控制浏览器关闭或退出
driver.quit()  # 退出浏览器
driver.close() # 退出当前页面