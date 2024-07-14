from selenium import webdriver
from time import sleep
import pandas as pd

file_path = "C:/Users/V/Desktop/bumble.xlsx"
excel_sheet = pd.read_excel(file_path)

excel_sheet['Name'] = excel_sheet['Name'].astype(str)


driver_path = 'C:/Users/V/Desktop/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome('C:/Users/V/Desktop/chromedriver.exe')

    def login(self):
        self.driver.get('https://bumble.com/get-started')
        sleep(3)

        fb_btn = bot.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/button')
        fb_btn.click()

        sleep(25)

        
        #switch pages
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
    
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('spac3ali3n@gmail.com')

        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys('Hellovichu!!')

    


        sleep(2)
        

        sleep(3)
        self.driver.switch_to_window(base_window)
        sleep(10)

TinderBot()