from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
PATH = "/home/amal/GRIP_Internship/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.thesparksfoundationsingapore.org/")
title=driver.title;
if title=="The Sparks Foundation | Home":
    print("Page Title name is correct")
else:
    print("Wrong Title Name")


print ("The test is completed")
driver.close()