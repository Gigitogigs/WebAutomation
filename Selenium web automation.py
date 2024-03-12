from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
options=Options()
options.add_experimental_option("detach", True)#Prevents auotmatic closure of page

driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://www.instagram.com/gigito.gigs")#goes to url
driver.maximize_window()#maximizes window
time.sleep(3)

login_btn = driver.find_element_by_class_name("")
login_btn.click()#Click on the login button