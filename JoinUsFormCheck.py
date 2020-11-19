from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

fullname = "Amal Mohan K"
email = "xyz@gmail.com"
PATH = "/home/amal/GRIP_Internship/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.thesparksfoundationsingapore.org/join-us/why-join-us/#")
element = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]")
element.send_keys(fullname)
element = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]")
element.send_keys(email)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/select/option[2]").click()
element.send_keys(Keys.RETURN)
print("The test is completed Successfully By submitting form data")
driver.close()
