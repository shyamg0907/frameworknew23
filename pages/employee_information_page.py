import logging
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from base.base_driver import BaseDriver
from utilities.utils import Utils


class EmployeeOtherInforamtion(BaseDriver):
    log=Utils.custom_logger()
    def __init__(self,driver,wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    def clickonleavetab(self):
        link_leave_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[@id='ui-accordion-2-header-1']")))
        link_leave_tab.click()
        time.sleep(2)
        self.log.info("Click on Leave tab")


    def employeeleaveaddtab(self):
        link_employee_leave_tab = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Employee Leave Add")))
        link_employee_leave_tab.click()
        self.log.info("Click on Leave Add tab")
        time.sleep(2)

    def selectdate(self,leavedate):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='txtstart']"))).click()
        time.sleep(3)
        # all_dates = self.driver.find_element(By.XPATH, "//td[text()='25']")
        all_dates=self.driver.find_elements(By.XPATH,"//div[@id='dp-popup']//td")


        for dateelement in all_dates:
            date=dateelement.text
            print(date)
            if date == leavedate:
                dateelement.click()
                self.log.warning("Date selected")
                break

