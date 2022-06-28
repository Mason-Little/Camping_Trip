from selenium import webdriver
import time
import keyboard
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=400x400')
driver = webdriver.Chrome("D:\\chromedriver.exe")
driver.implicitly_wait(30)
# driver.minimize_window()

driver.get("https://camping.bcparks.ca/")

def search_bar():
    '''searchs for the park'''
    # clicking search bar
    driver.find_element(By.XPATH,'//*[@id="park-autocomplete"]').click()
    # entering the search term
    driver.find_element(By.XPATH,'//*[@id="park-autocomplete"]').send_keys("Por")
    # pressing top result
    driver.find_element(By.XPATH,'//*[@id="park-autocomplete"]').send_keys(Keys.ENTER)


def filter():
    # click on the filter button
    driver.find_element(By.XPATH,'//*[@id="mat-select-value-1"]').click()
    # selecting Type
    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div/div/mat-option[4]').click()
    # pressing search
    driver.find_element(By.XPATH,'//*[@id="actionSearch"]/span[1]/div[2]').click()


def searching_camp_sites_A():
    # Press On List View
    driver.find_element(By.XPATH,'//*[@id="list-view-button"]/fa-icon').click()
    # Unpress Show All
    driver.find_element(By.XPATH,'//*[@id="mat-checkbox-1"]').click()
    # Press a Site
    driver.find_element(By.XPATH,'//*[@id="mat-expansion-panel-header-1"]').click()
    # Pressing Calendar View
    driver.find_element(By.XPATH,'//*[@id="mat-tab-label-1-2"]').click()
    driver.find_element(By.XPATH,'//*[@id="mat-checkbox-2"]/label/span[1]').click()
    # Unpress show all
    rows = driver.find_elements(By.XPATH,"//table/tbody/tr")
    print(len(rows))
    # for i in range(0, len(rows)):
    #     for y in range(0, 14):
    # btn = driver.find_element_by_css_selector(f'#resource-cell-{i}-{y}').get_attribute("aria-label")
    # print(btn)


def searching_camp_sites_B():
    # click back on Porteau Cove
    driver.find_element(By.XPATH,'//*[@id="breadcrumb"]/li[3]/button').click()
    # click on list View
    driver.find_element(By.XPATH,'//*[@id="mat-tab-label-1-1"]').click()
    # Uncheck Show All
    driver.find_element(By.XPATH,'//*[@id="mat-checkbox-41"]').click()
    # Press B Site
    driver.find_element(By.XPATH,'//*[@id="mat-expansion-panel-header-6"]/span/mat-panel-title').click()
    # Click on Calendar View
    driver.find_element(By.XPATH,'//*[@id="grid-view-button"]').click()
    # Unpressed Show All
    driver.find_element(By.XPATH,'//*[@id="mat-checkbox-42"]/label/span[1]').click()
    # for i in range(0, 7):
    #     for y in range(0, 14):
    #         btn = driver.find_element_by_css_selector(f'#resource-cell-{i}-{y}').get_attribute("aria-label")
    #         print(btn)

def searching_camp_sites_C():
    # click back on Porteau Cove
    driver.find_element(By.XPATH,'//*[@id="breadcrumb"]/li[3]/button').click()
    # click on list View
    driver.find_element(By.XPATH,'//*[@id="mat-tab-label-1-1"]').click()
    # Uncheck Show All
    driver.find_element(By.XPATH,'//*[@id="mat-checkbox-51"]').click()
    # Press Walk In Site
    driver.find_element(By.XPATH,'//*[@id="mat-expansion-panel-header-11"]/span/mat-panel-description').click()
    # Click on Calendar View
    driver.find_element(By.XPATH,'//*[@id="grid-view-button"]/fa-icon/svg').click()



search_bar()
input("Press Enter to continue shearching")
filter()
input("Press Enter to continue fitler")
searching_camp_sites_A()
input("Press Enter to continue a")
searching_camp_sites_B()
input("Press Enter to continue b")
searching_camp_sites_C()


