import time
import smtplib
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import ssl
from email.message import EmailMessage

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
    driver.find_element(By.XPATH, '//*[@id="park-autocomplete"]').click()
    # entering the search term
    driver.find_element(By.XPATH, '//*[@id="park-autocomplete"]').send_keys("Por")
    # pressing top result
    driver.find_element(By.XPATH, '//*[@id="park-autocomplete"]').send_keys(Keys.ENTER)
    # click on the filter button
    driver.find_element(By.XPATH, '//*[@id="mat-select-value-1"]').click()
    # Selecting Type
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="mat-option-3"]').click()
    # Pressing search
    driver.find_element(By.XPATH, '//*[@id="actionSearch"]').click()


def CampSite_A():
    # Press On List View
    driver.find_element(By.XPATH, '//*[@id="list-view-button"]').click()
    # Un Press Show All
    driver.find_element(By.XPATH, '//*[@id="mat-checkbox-1"]/label/span[1]').click()
    # Press a Site
    driver.find_element(By.XPATH, '//*[@id="ListView"]/div/div[2]/mat-accordion/mat-expansion-panel[1]').click()
    # Pressing Calendar View
    driver.find_element(By.XPATH, '//*[@id="grid-view-button"]').click()
    # Un Press show all
    driver.find_element(By.XPATH, '//*[@id="mat-checkbox-2"]/label/span[1]').click()
    for i in range(0, 37):
        for y in range(0, 14):
            btn = driver.find_element_by_css_selector(f'#resource-cell-{i}-{y}').get_attribute("aria-label")
            btn = btn.split(' ')
            btn = list(filter(None, btn))
            answer = btn.pop(-1)
            btn = ' '.join(btn)
            btn = btn.replace('\n', '')
            btn = btn.replace('\r', '')
            btn = btn.strip()
            CampSite_A_Dict[btn] = answer


def CampSite_B():
    # Back To Porteau Cove
    driver.find_element(By.XPATH, '//*[@id="breadcrumb"]/li[3]/button').click()
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
            btn = btn.split(' ')
            btn = list(filter(None, btn))
            answer = btn.pop(-1)
            btn = ' '.join(btn)
            btn = btn.replace('\n', '')
            btn = btn.replace('\r', '')
            btn = btn.strip()
            CampSite_B_Dict[btn] = answer


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
            btn = btn.split(' ')
            btn = list(filter(None, btn))
            answer = btn.pop(-1)
            btn = ' '.join(btn)
            btn = btn.replace('\n', '')
            btn = btn.replace('\r', '')
            btn = btn.strip()
            CampSite_C_Dict[btn] = answer


CampSite_A_Dict = {}
CampSite_B_Dict = {}
CampSite_C_Dict = {}

search_and_filter()
CampSite_A()
time.sleep(2)
CampSite_B()
time.sleep(2)
CampSite_C()

print(CampSite_A_Dict)
print(CampSite_B_Dict)
print(CampSite_C_Dict)

#constants

email_sender = 'python.driving.port@gmail.com'
email_password = 'ressubtezngvojdg'
email_receiver = 'baboom16mll@gmail.com'

for k in CampSite_A_Dict:
    compare = CampSite_A_Dict[k].lower
    if CampSite_A_Dict[k] == "Available":
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, k)
            print(f'Email sent to {email_receiver}')
            smtp.quit()
    input("Press Enter to continue...")

for k in CampSite_B_Dict:
    compare = CampSite_A_Dict[k].lower
    if CampSite_A_Dict[k].lower == "Available":
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, k)
            print(f'Email sent to {email_receiver}')
            smtp.quit()

for k in CampSite_C_Dict:
    compare = CampSite_A_Dict[k].lower
    if CampSite_A_Dict[k].lower == "Available":
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, k)
            print(f'Email sent to {email_receiver}')
            smtp.quit()

driver.quit()
