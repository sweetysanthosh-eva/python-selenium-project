import pytest
from selenium.webdriver.common.by import By

from Constant import Constants
from Pages.Homepage import Homepage
from Pages.Loginpage import Loginpage
from Utilities.ExcelUtility import ExcelUtility


class Testhome:
    @pytest.mark.description("Login with valid credentials and verify logout")
    @pytest.mark.flaky(rerun=2)
    def test_logout(self,crossbrowser):
        self.driver=crossbrowser
        self.driver.get(Constants.URL)
        self.driver.maximize_window()
        excelutility = ExcelUtility(Constants.FILEPATH)
        username = excelutility.get_string_data(2, 1, Constants.LOGINPAGE)
        password = excelutility.get_string_data(2, 2, Constants.LOGINPAGE)
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username).enter_password(password)
        homepage = loginpage.click_login()
        #loginpage.enter_password(password)
        #loginpage.click_login()
        #homepage = Homepage(self.driver)
        homepage.click_admin()
        loginpage=homepage.click_logout()

        """admin=self.driver.find_element(By.XPATH, "//a[@data-toggle='dropdown']")
        admin.click()
        logouticon=self.driver.find_element(By.XPATH, "//i[@class='ace-icon fa fa-power-off']")
        logouticon.click()"""

        currenturl = self.driver.current_url
        assert currenturl == "https://groceryapp.uniqassosiates.com/admin/login"

