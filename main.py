import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=400x400')
driver = webdriver.Chrome("D:\\chromedriver.exe")
driver.implicitly_wait(10)
# driver.minimize_window()

driver.get("https://camping.bcparks.ca/")

def search_and_filter():
    '''searchs for the park'''
    # clicking search bar
    driver.find_element(By.XPATH,'//*[@id="park-autocomplete"]').click()
    # entering the search term
    driver.find_element(By.XPATH,'//*[@id="park-autocomplete"]').send_keys("Por")
    # pressing top result
    driver.find_element(By.XPATH,'//*[@id="park-autocomplete"]').send_keys(Keys.ENTER)
    # click on the filter button
    driver.find_element(By.XPATH,'//*[@id="mat-select-value-1"]').click()
    # Selecting Type
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="mat-option-3"]').click()
    # Pressing search
    driver.find_element(By.XPATH,'//*[@id="actionSearch"]').click()

def CampSite_A():
    # Press On List View
    driver.find_element(By.XPATH,'//*[@id="list-view-button"]').click()
    # Un Press Show All
    driver.find_element(By.XPATH,'//*[@id="mat-checkbox-1"]/label/span[1]').click()
    # Press a Site
    driver.find_element(By.XPATH,'//*[@id="ListView"]/div/div[2]/mat-accordion/mat-expansion-panel[1]').click()
    # Pressing Calendar View
    driver.find_element(By.XPATH,'//*[@id="grid-view-button"]').click()
    # Un Press show all
    driver.find_element(By.XPATH,'//*[@id="mat-checkbox-2"]/label/span[1]').click()
    # for i in range(0, 37):
    #     for y in range(0, 14):
    #         btn = driver.find_element_by_css_selector(f'#resource-cell-{i}-{y}').get_attribute("aria-label")
    #         print(btn)

def CampSite_B():
    # Back To Porteau Cove
    driver.find_element(By.XPATH,'//*[@id="breadcrumb"]/li[3]/button').click()
    # Press On List View
    driver.find_element(By.XPATH, '//*[@id="list-view-button"]').click()
    # Un Press Show All
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="mat-checkbox-41"]/label/span[1]').click()
    # Press On B
    driver.find_element(By.XPATH, '//*[@id="ListView"]/div/div[2]/mat-accordion/mat-expansion-panel[2]').click()
    # Pressing Calendar View
    driver.find_element(By.XPATH, '//*[@id="grid-view-button"]').click()
    # Un Press show all
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="mat-checkbox-42"]/label').click()
    for i in range(0, 7):
        for y in range(0, 14):
            btn = driver.find_element_by_css_selector(f'#resource-cell-{i}-{y}').get_attribute("aria-label")
            print(btn)

def CampSite_C():
    # Back To Porteau Cove
    driver.find_element(By.XPATH, '//*[@id="breadcrumb"]/li[3]/button').click()
    # Press On List View
    driver.find_element(By.XPATH, '//*[@id="list-view-button"]').click()
    # Un Press Show All
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="mat-checkbox-51"]/label').click()
    # Press On C
    driver.find_element(By.XPATH, '//*[@id="ListView"]/div/div[2]/mat-accordion/mat-expansion-panel[3]').click()
    # Pressing Calendar View
    driver.find_element(By.XPATH, '//*[@id="grid-view-button"]').click()
    # Un Press show all
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="mat-checkbox-52"]/label').click()
    for i in range(0, 16):
        for y in range(0, 14):
            btn = driver.find_element_by_css_selector(f'#resource-cell-{i}-{y}').get_attribute("aria-label")
            print(btn)





search_and_filter()
CampSite_A()
time.sleep(2)
CampSite_B()
time.sleep(2)
CampSite_C()