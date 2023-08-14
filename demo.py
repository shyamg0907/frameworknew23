import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

from selenium.webdriver.support.select import Select


# driver=webdriver.Chrome(ChromeDriverManager().install())
s=Service(executable_path='F:\\SHyam_9July2023\\newSoftware\\chromedriver-win32\\chromedriver.exe')
driver=webdriver.Chrome(service=s)

driver.get("https://pms.mrccsolutions.com/")
driver.maximize_window()