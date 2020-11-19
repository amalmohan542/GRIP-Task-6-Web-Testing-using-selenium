
# Selenium to Check whether Executive Team members Images Exist or not

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
PATH = "/home/amal/GRIP_Internship/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.thesparksfoundationsingapore.org/about/executive-team/")
elem1 = bool
elem2 = bool
elem1 =driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[1]/a/img")
elem2 =driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[3]/a/img")
if elem1 and elem2:
    print("Executive Team members Images Exist")
else:
    print("Executive Team members Images is Missing")

time.sleep(2)
driver.quit()
print ("The test is completed")


