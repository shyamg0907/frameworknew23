import time

import pytest

from pages.yatra_launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    def test_search_flights(self):
        lp=LaunchPage(self.driver, self.wait)
        print("succesfully launched browser")
        lp.closepopup()
        time.sleep(4)
        lp.departfrom("New Delhi")
        lp.goingto("New York")
        lp.selectdate("24/08/2023")
        lp.clicksearch()

        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(1)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            if lastCount == pageLength:
                match = True
        time.sleep(4)




