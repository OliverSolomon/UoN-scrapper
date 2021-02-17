"""This script populates fields with user data generated """

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
from time import sleep
from requests import get

from data import uname, passwd

# def getText():

url = r"https://multimedia.uonbi.ac.ke/"

#initiated driver
driver = webdriver.Chrome(executable_path="/home/gamin3/Desktop/Ghosts-main/Ghosts-beta/chromedriver/chromedriverV88.0.4324.150")


# +++++++++++++++++++++    XPATHS    +++++++++++++++++++++++++
unameXpath = ''
passwdXpath = ''
formSubmitXpath = ''


# +++++++++++++++++++++    FUNCTIONALITY    ++++++++++++++++++

#initialising
driver.get(url)

#log in page
driver.find_element_by_xpath(unameXpath).send_keys()
driver.find_element_by_xpath(passwdXpath).send_keys()
driver.find_element_by_xpath(formSubmitXpath).click()