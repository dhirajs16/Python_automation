from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome()


columns = ['Symbol_no', 'Name', 'College', 'GPA']
student = pd.DataFrame(columns=columns)


url = "http://103.175.192.30:86/Result"
driver.get(url)
driver.maximize_window()


for num in range(453, 794):
    


    input_element = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/a/span""")
    # Clear the input field (optional)
    ActionChains(driver).move_to_element(input_element).click().send_keys(Keys.CONTROL + "").send_keys(Keys.DELETE).perform()
    # Send your desired value
    ActionChains(driver).move_to_element(input_element).send_keys("BIT Fourth Semester"+Keys.ENTER).perform()





    first_input = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div/div[3]/div/div[2]/div/div/form/div[2]/div[2]/input""")
    first_input.clear()
    first_input.send_keys(f"BIT {num}/078")




    second_input = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div/div[3]/div/div[2]/div/div/form/div[3]/div[2]/input""")
    second_input.clear()
    second_input.send_keys(f"BIT {num}/078"+Keys.ENTER)

    time.sleep(0.1)

    #web scraping
    symbolno = driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div/div[4]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/th[2]/span""").text
    name = driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div/div[4]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/th[1]/span""").text
    college = driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div/div[4]/div/div[2]/div/div[2]/div/table/tbody/tr[2]/th/span""").text
    gpa = driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div/div[4]/div/div[2]/div/div[3]/div/div/table[1]/tfoot/tr[2]/td[3]/span""").text



    student = student._append({'Symbol_no':symbolno, 'Name': name, 'College':college, 'GPA': gpa}, ignore_index=True)
    student.to_csv('./student_table.csv', index = False)

time.sleep(100)




