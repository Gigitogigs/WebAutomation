from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from secret import PASSWORD, USERNAME

posts = []


options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

options.add_experimental_option("detach", True)

url = "https://www.instagram.com/?hl=en"

keyword = "google"


driver.get(url)

time.sleep(5) 

username_box = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
username_box.send_keys(USERNAME)

username_box = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
username_box.send_keys(PASSWORD)

time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()

time.sleep(10)

driver.get('https://www.instagram.com/?next=%2F&hl=en')

time.sleep(6)

driver.find_element(By.XPATH, '//button[text()="Not Now"]').click()

time.sleep(3)

driver.get(f'https://www.instagram.com/{keyword}/?hl=en')

time.sleep(5)

posts = driver.find_elements(By.CLASS_NAME, '_aagw')




# iterate through the first 5 posts
for i in range(5):
    for post in posts:
        post.click()

        #like

        time.sleep(3)

        driver.find_element(By.CLASS_NAME, 'xp7jhwk').click()

        time.sleep(2)

        # comment

        text_area = driver.find_element(By.TAG_NAME, 'textarea').click()

        time.sleep(3)

        cpmment = driver.find_element(By.CLASS_NAME, 'focus-visible').send_keys("Awesome!")

        time.sleep(1)

        driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/div[2]/div').click()

        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div/div[2]").click()




# driver.quit()
