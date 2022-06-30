import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
import ssl

url = "https://camping.bcparks.ca/create-booking/results?resourceLocationId=-2147483550&mapId=-2147483449&searchTabGroupId=0&bookingCategoryId=0&startDate=2022-07-01&endDate=2022-07-02&nights=1&isReserving=true&equipmentId=-32768&subEquipmentId=-32765&partySize=1&searchTime=2022-06-29T17:56:38.426"

for i in range(1, 500):
    def campsite_a():
        try:
            driver_a = webdriver.Chrome("D:\\chromedriver.exe")
            driver_a.implicitly_wait(10)
            driver_a.get(url)
            # driver.minimize_window()
            # Press On List View
            time.sleep(1)
            driver_a.find_element(By.XPATH, '//*[@id="list-view-button"]').click()
            # Un Press Show All
            driver_a.find_element(By.XPATH, '//*[@id="mat-checkbox-1"]/label/span[2]/div').click()
            # input("Press Enter to continue...")
            # Press a Site
            driver_a.find_element(By.XPATH, '//*[@id="ListView"]/div/div[2]/mat-accordion/mat-expansion-panel[1]').click()
            # Pressing Calendar View
            time.sleep(1)
            driver_a.find_element(By.XPATH, '//*[@id="grid-view-button"]').click()
            # Un Press show all
            driver_a.find_element(By.XPATH, '//*[@id="mat-checkbox-2"]/label/span[2]/div').click()
            for i in range(0, 37):
                for y in range(0, 14):
                    btn = driver_a.find_element(By.CSS_SELECTOR, f'#resource-cell-{i}-{y}').get_attribute("aria-label")
                    btn = btn.split(' ')
                    btn = list(filter(None, btn))
                    answer = btn.pop(-1)
                    btn = ' '.join(btn)
                    btn = btn.replace('\n', '')
                    btn = btn.replace('\r', '')
                    btn = btn.strip()
                    CampSite_Dict[btn] = answer
            driver_a.quit()
        except:
            pass


    def campsite_b():
        try:
            driver_b = webdriver.Chrome("D:\\chromedriver.exe")
            driver_b.implicitly_wait(10)
            driver_b.get(url)
            # Pressing List View
            driver_b.find_element(By.XPATH, '//*[@id="list-view-button"]').click()
            # Un Press Show All
            driver_b.find_element(By.XPATH, '//*[@id="mat-checkbox-1"]/label/span[2]/div').click()
            # input("Press Enter to continue...")
            # Press On B
            driver_b.find_element(By.XPATH, '//*[@id="ListView"]/div/div[2]/mat-accordion/mat-expansion-panel[2]').click()
            # Pressing Calendar View
            driver_b.find_element(By.XPATH, '//*[@id="grid-view-button"]').click()
            # Un Press show all
            time.sleep(3)
            driver_b.find_element(By.XPATH, '//*[@id="mat-checkbox-2"]/label/span[2]/div').click()
            for i in range(0, 7):
                for y in range(0, 14):
                    btn = driver_b.find_element(By.CSS_SELECTOR, f'#resource-cell-{i}-{y}').get_attribute("aria-label")
                    btn = btn.split(' ')
                    btn = list(filter(None, btn))
                    answer = btn.pop(-1)
                    btn = ' '.join(btn)
                    btn = btn.replace('\n', '')
                    btn = btn.replace('\r', '')
                    btn = btn.strip()
                    CampSite_Dict[btn] = answer
            driver_b.quit()
        except:
            pass


    def CampSite_C():
        try:
            driver_c = webdriver.Chrome("D:\\chromedriver.exe")
            driver_c.implicitly_wait(10)
            driver_c.get(url + '')
            time.sleep(3)
            # Pressing List View
            driver_c.find_element(By.XPATH, '//*[@id="list-view-button"]').click()
            # Un Press Show All
            driver_c.find_element(By.XPATH, '//*[@id="mat-checkbox-1"]/label/span[2]/div').click()
            # input("Press Enter to continue...")
            # Press On C
            driver_c.find_element(By.XPATH, '//*[@id="ListView"]/div/div[2]/mat-accordion/mat-expansion-panel[3]').click()
            # Pressing Calendar View
            driver_c.find_element(By.XPATH, '//*[@id="grid-view-button"]').click()
            # Un Press show all
            time.sleep(3)
            driver_c.find_element(By.XPATH, '//*[@id="mat-checkbox-2"]/label/span[2]/div').click()
            # input("Press Enter to continue...")
            for i in range(0, 16):
                for y in range(0, 14):
                    btn = driver_c.find_element(By.CSS_SELECTOR, '#resource-cell-{i}-{y}').get_attribute("aria-label")
                    btn = btn.split(' ')
                    btn = list(filter(None, btn))
                    answer = btn.pop(-1)
                    btn = ' '.join(btn)
                    btn = btn.replace('\n', '')
                    btn = btn.replace('\r', '')
                    btn = btn.strip()
                    CampSite_Dict[btn] = answer
            driver_c.quit()
        except:
            pass


    CampSite_Dict = {}

    campsite_a()
    time.sleep(2)
    campsite_b()
    time.sleep(2)
    CampSite_C()

    # Constants

    email_sender = 'python.driving.port@gmail.com'
    email_password = 'ressubtezngvojdg'
    email_receiver = 'baboom16mll@gmail.com'

    for k in CampSite_Dict:
        print(CampSite_Dict[k])
        compare = CampSite_Dict[k].lower()
        if compare == "available":
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, k)
                print(f'Email sent to {email_receiver}')
                smtp.quit()
    print("Done", i)
    # time.sleep(300)