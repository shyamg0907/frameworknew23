import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException,StaleElementReferenceException,ElementNotSelectableException,NoAlertPresentException


class LaunchPage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def closepopup(self):
        print("enter closepopou")
        handle1=self.driver.window_handles
        time.sleep(3)
        self.driver.switch_to.window(handle1)
        print("handle window")
        self.driver.find_element(By.XPATH,"//a[@id='webklipper-publisher-widget-container-notification-close-div']").click()
        time.sleep(4)

    def departfrom(self, departlocation):
        depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        time.sleep(2)
        depart_from.click()
        depart_from.send_keys(departlocation)
        depart_from.send_keys(Keys.ENTER)

    def goingto(self, gointolocation):
        going_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        going_to.click()
        time.sleep(2)
        going_to.send_keys(gointolocation)
        search_results = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]/li")))

        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                break
        going_to.send_keys(Keys.ENTER)

    def selectdate(self, departuredate):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        all_dates = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))\
        .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break

    def clicksearch(self):
        self.driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
        time.sleep(3)
