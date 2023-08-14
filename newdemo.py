from selenium.webdriver.chrome.service import Service
from selenium import webdriver

s=Service('F:\\SHyam_9July2023\\newSoftware\\chromedriver-win32\\chromedriver.exe')
driver=webdriver.Chrome(service=s)

driver.get("https://pms.mrccsolutions.com/")
driver.maximize_window()
print(driver.title)
driver.close()