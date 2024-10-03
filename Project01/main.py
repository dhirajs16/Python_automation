from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')


    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://www.datacamp.com/users/sign_in')
    return driver


def main():
    driver = get_driver()
    # time.sleep(2)
    driver.find_element(by='id', value='user_email').send_keys('sp4105043@gmail.com' + Keys.RETURN)
    time.sleep(2)
    button = driver.find_element(by='xpath', value='/html/body/div[1]/div[2]/div/div/div[3]/form/button')
    action = ActionChains(driver)
    action.double_click(button).perform()
    
    time.sleep(5)



    # driver.execute_script("arguments[0].click();", button) 
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[3]/form/button'))).click()
    time.sleep(5)



main()
