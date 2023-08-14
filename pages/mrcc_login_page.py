import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException,StaleElementReferenceException,ElementNotSelectableException,NoAlertPresentException

from base.base_driver import BaseDriver
from utilities.utils import Utils


class LaunchPage(BaseDriver):
    log = Utils.custom_logger()
    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait


    def usernamefeild(self, loginusername):
        textbox_username_name = self.wait.until(EC.element_to_be_clickable((By.NAME, "txtUserName")))
        time.sleep(2)
        textbox_username_name.click()
        textbox_username_name.send_keys(loginusername)
        self.log.info("Username added")
        # textbox_username_name.send_keys(Keys.ENTER)

    def passwordfeild(self, loginpassword):
        textbox_password_name = self.wait.until(EC.element_to_be_clickable((By.NAME, "txtPassword")))
        time.sleep(2)
        textbox_password_name.click()
        textbox_password_name.send_keys(loginpassword)
        self.log.info("Password added")
        # textbox_password_name.send_keys(Keys.ENTER)

    # def selectdate(self, departuredate):
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
    #     all_dates = self.wait.until(
    #         EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))\
    #     .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
    #
    #     for date in all_dates:
    #         if date.get_attribute("data-date") == departuredate:
    #             date.click()
    #             break

    def submitlogin(self):
        self.driver.find_element(By.XPATH, "//input[@name='BtnSubmitLogin']").click()
        time.sleep(3)
        self.log.warning("Click on Submit button")
