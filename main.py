from selenium import webdriver
import time
import keyboard
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=400x400')
driver = webdriver.Chrome("D:\\chromedriver.exe")
# driver.minimize_window()

driver.get("https://camping.bcparks.ca/")

def search_bar():
    '''searchs for the park'''
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="park-autocomplete"]').click()
    driver.find_element_by_xpath('//*[@id="park-autocomplete"]').send_keys("p")
    driver.find_element_by_xpath('//*[@id="park-autocomplete"]').send_keys("o")
    driver.find_element_by_xpath('//*[@id="park-autocomplete"]').send_keys("r")
    driver.find_element_by_xpath('//*[@id="park-autocomplete"]').send_keys(Keys.ENTER)

search_bar()
driver.find_element_by_xpath('//*[@id="mat-select-value-1"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="mat-option-3"]/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="actionSearch"]/span[1]/div[2]').click()


