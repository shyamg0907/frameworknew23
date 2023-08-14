import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.support.select import Select

class TestPMS():

# driver=webdriver.Chrome(ChromeDriverManager().install())
    def test_pms(self):
        s=Service('F:\\SHyam_9July2023\\newSoftware\\chromedriver-win32\\chromedriver.exe')
        driver=webdriver.Chrome(service=s)

        driver.get("https://pms.mrccsolutions.com/")
        driver.maximize_window()
        print(driver.title)
        driver.close()

tpms=TestPMS()
tpms.test_pms()
