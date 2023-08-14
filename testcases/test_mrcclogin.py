import time

import pytest
import softest
import openpyxl

from pages.employee_information_page import EmployeeOtherInforamtion
from pages.mrcc_login_page import LaunchPage
from utilities.utils import Utils
from ddt import ddt,data,file_data,unpack


@pytest.mark.usefixtures("setup")
# @ddt
class TestMRCCLogin(softest.TestCase):
    log = Utils.custom_logger()

    @data(*Utils.read_data_from_excel("C:\\Users\\SHYAM GUPTA\\PycharmProjects\\frameworknew23\\testdata\\testdataexcel.xlsx","Sheet1"))
    @unpack
    def test_search_flights(self,loginusername,loginpassword,leavedate):
        lp=LaunchPage(self.driver, self.wait)
        self.log.info("succesfully launched browser")
        lp.usernamefeild(loginusername)
        lp.passwordfeild(loginpassword)
        lp.submitlogin()
        time.sleep(3)

        eoi = EmployeeOtherInforamtion(self.driver, self.wait)
        eoi.clickonleavetab()
        time.sleep(3)
        eoi.employeeleaveaddtab()
        time.sleep(4)
        eoi.selectdate(leavedate)
        time.sleep(4)

    # Through json data file
    # @file_data("../testdata/testdata.json")
    # def test_search_flights(self, loginusername,loginpassword,leavedate):
    #     lp = LaunchPage(self.driver, self.wait)
    #     self.log.info("succesfully launched browser")
    #     lp.usernamefeild(loginusername)
    #     lp.passwordfeild(loginpassword)
    #     lp.submitlogin()
    #     time.sleep(3)
    #
    #     eoi = EmployeeOtherInforamtion(self.driver, self.wait)
    #     eoi.clickonleavetab()
    #     time.sleep(3)
    #     eoi.employeeleaveaddtab()
    #     time.sleep(4)
    #     eoi.selectdate(leavedate)
    #     time.sleep(4)

    # THROUGH DDT
    # @data(("sagupta@mrccsolutions.com","pass@word1","18"),("sagupta@mrccsolutions.com","pass@word1","27"))
    # @unpack
    # def test_search_flights(self,loginusername,loginpassword,leavedate):
    #     lp=LaunchPage(self.driver, self.wait)
    #     self.log.info("succesfully launched browser")
    #     lp.usernamefeild(loginusername)
    #     lp.passwordfeild(loginpassword)
    #     lp.submitlogin()
    #     time.sleep(3)
    #
    #     eoi = EmployeeOtherInforamtion(self.driver, self.wait)
    #     eoi.clickonleavetab()
    #     time.sleep(3)
    #     eoi.employeeleaveaddtab()
    #     time.sleep(4)
    #     eoi.selectdate(leavedate)
    #     time.sleep(4)


    # def test_search_flights(self):
    #     lp=LaunchPage(self.driver, self.wait)
    #     self.log.info("succesfully launched browser")
    #     lp.usernamefeild("sagupta@mrccsolutions.com")
    #     lp.passwordfeild("pass@word1")
    #     lp.submitlogin()
    #     time.sleep(3)
    #
    #     eoi = EmployeeOtherInforamtion(self.driver, self.wait)
    #     eoi.clickonleavetab()
    #     time.sleep(3)
    #     eoi.employeeleaveaddtab()
    #     time.sleep(4)
    #     eoi.selectdate("17")
    #     time.sleep(4)






        # pageLength = self.driver.execute_script(
        #     "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        # match = False
        # while (match == False):
        #     lastCount = pageLength
        #     time.sleep(1)
        #     pageLength = self.driver.execute_script(
        #         "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        #     if lastCount == pageLength:
        #         match = True
        # time.sleep(4)




