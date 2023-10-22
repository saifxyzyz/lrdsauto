from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
import time
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.lordsautomation.com/Login.aspx")
username = driver.find_element(By.ID, 'txtUserName')
next = driver.find_element(By.ID, 'btnNext')

    

def websitenav(x):
    try:
        time.sleep(5)
        username = driver.find_element(By.ID, 'txtUserName')
        next = driver.find_element(By.ID, 'btnNext')
        username.send_keys(x)
        next.click()
        password = driver.find_element(By.ID, 'txtPassword')
        password.send_keys(x)
        submit = driver.find_element(By.ID, 'btnSubmit')
        submit.click()
        marks = driver.find_element(By.ID, 'ctl00_cpStud_lnkOverallMarksSemwiseMarks')
        marks.click()
    except:
        websitenav(x)
    return(driver.find_element(By.XPATH, "/html/body").text+'\n'+x*10)