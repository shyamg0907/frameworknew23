import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    # s = Service('F:\\SHyam_9July2023\\newSoftware\\chromedriver-win32\\chromedriver.exe')
    # driver = webdriver.Chrome(service=s)
    option1=Options()
    option1.add_argument("--disable-notifications")
    # option1.add_experimental_option("detach", True)
    driver=webdriver.Chrome(executable_path="F:\\SHyam_9July2023\\newSoftware\\chromedriver-win32\\chromedriver.exe")
    wait = WebDriverWait(driver, 10)
    driver.get("https://pms.mrccsolutions.com/login.php")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.close()