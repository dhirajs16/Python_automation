from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = webdriver.ChromeOptions()
    
    # Disables the infobar that shows "Chrome is being controlled by automated test software"
    options.add_argument('disable-infobars')
    
    # Starts the browser maximized to the screen size
    options.add_argument('start-maximized')
    
    # Overcomes limited resource problems in Docker containers
    options.add_argument('disable-dev-shm-usage')
    
    # Disables the sandbox for Chrome, useful for running in containers
    options.add_argument('no-sandbox')
    
    # Prevents Chrome from being detected as automated
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    
    # Disables the "Automation Controlled" message in Chrome
    options.add_argument('disable-blink-features=AutomationControlled')


    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://dhirajs16.github.io/cv/')
    return driver


driver = get_driver()
element = driver.find_element(by='xpath', value='/html/body/h3[1]')

print(element.text)