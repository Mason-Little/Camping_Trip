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
    time.sleep(6)
    # clicking search bar
    driver.find_element_by_xpath('//*[@id="park-autocomplete"]').click()
    # entering the search term
    driver.find_element_by_xpath('//*[@id="park-autocomplete"]').send_keys("Por")
    # pressing top result
    driver.find_element_by_xpath('//*[@id="park-autocomplete"]').send_keys(Keys.ENTER)


def filter():
    # click on the filter button
    driver.find_element_by_xpath('//*[@id="mat-select-value-1"]').click()
    time.sleep(3)
    # selecting Type
    driver.find_element_by_xpath('//*[@id="mat-option-3"]').click()
    time.sleep(1)
    # pressing search
    driver.find_element_by_xpath('//*[@id="actionSearch"]/span[1]/div[2]').click()


def searching_camp_sites_A():
    # Press On List View
    driver.find_element_by_xpath('//*[@id="list-view-button"]/fa-icon').click()
    time.sleep(1)
    # Unpress Show All
    driver.find_element_by_xpath('//*[@id="mat-checkbox-1"]/label/span[1]').click()
    time.sleep(1)
    # Press a Site
    driver.find_element_by_xpath('//*[@id="mat-expansion-panel-header-1"]').click()
    time.sleep(1)
    # Pressing Calendar View
    driver.find_element_by_xpath('//*[@id="mat-tab-label-1-2"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="mat-checkbox-2"]/label/span[1]').click()
    time.sleep(1)
    # Unpress show all
    rows = driver.find_elements_by_xpath("//table/tbody/tr")
    print(len(rows))
    # for i in range(0, len(rows)):
    #     for y in range(0, 14):
    # btn = driver.find_element_by_css_selector(f'#resource-cell-{i}-{y}').get_attribute("aria-label")
    # print(btn)


def searching_camp_sites_B():
    time.sleep(1)
    # click back on Porteau Cove
    driver.find_element_by_xpath('//*[@id="breadcrumb"]/li[3]/button').click()
    time.sleep(1)
    # click on list View
    driver.find_element_by_xpath('//*[@id="mat-tab-label-1-1"]').click()
    time.sleep(1)
    # Uncheck Show All
    driver.find_element_by_xpath('//*[@id="mat-checkbox-42"]/label/span[1]').click()
    time.sleep(1)
    # Press B Site
    driver.find_element_by_xpath('//*[@id="mat-expansion-panel-header-60"]').click()
    time.sleep(1)
    # Click on Calendar View
    driver.find_element_by_xpath('//*[@id="grid-view-button"]').click()
    time.sleep(1)
    # Unpressed Show All
    driver.find_element_by_xpath('//*[@id="mat-checkbox-7"]/label/span[1]').click()


search_bar()
filter()
time.sleep(3)
searching_camp_sites_A()
time.sleep(3)
searching_camp_sites_B()


