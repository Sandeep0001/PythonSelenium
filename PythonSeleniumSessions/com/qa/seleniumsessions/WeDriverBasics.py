from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome("C:\\Users\\sandeep.is\\PycharmProjects\\PythonSeleniumSessions\\drivers\\chromedriver.exe")

# caps = DesiredCapabilities.FIREFOX
# caps["maroonette"] = True
# caps["binary"] = "/"
# driver = webdriver.Firefox("C:\\Users\\sandeep.is\\PycharmProjects\\PythonSeleniumSessions\\drivers\\geckodriver.exe")

driver.get("https://www.freecrm.com/")

title1 = driver.title

print(title1)

#assert "#1 Free CRM software in the cloud for sales and service" in title1

driver.find_element_by_name("username").send_keys("y3te924psx1y")
driver.find_element_by_name("password").send_keys("1t6lxkTddupZ")

driver.quit()