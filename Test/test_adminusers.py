import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Constant import Constants
from Pages.Adminuserpage import Adminuserpage
from Pages.Loginpage import Loginpage
from Utilities.ExcelUtility import ExcelUtility


class Testadminusers:
    @pytest.mark.description("Check whether a new admin user is created after entering valid details and clicking Save")
    def test_admin(self,browserinstance):
        self.driver=browserinstance
        self.driver.get(Constants.URL)
        self.driver.maximize_window()
        excelutility = ExcelUtility(Constants.FILEPATH)
        username = excelutility.get_string_data(2, 1, Constants.LOGINPAGE)
        password = excelutility.get_string_data(2, 2, Constants.LOGINPAGE)
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username).enter_password(password).click_login().click_adminusertile().click_newbutton().enter_adminusername(username).enter_adminpassword(password).enter_usertype("Staff").click_savebutton()
        #loginpage.enter_password(password)
        #loginpage.click_login()
        adminuserpage=Adminuserpage(self.driver)
        #adminuserpage.click_adminusertile().click_newbutton().enter_adminusername(username).enter_adminpassword(password).enter_usertype("Staff").click_savebutton()
        #adminuserpage.click_newbutton()
        #adminuserpage.enter_adminusername(username)
        #adminuserpage.enter_adminpassword(password)
        #adminuserpage.enter_usertype("Staff")
        #adminuserpage.click_savebutton()

        """username_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        username_textbox.send_keys(username)
        password_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_textbox.send_keys(password)
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
        adminusertile=self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin'and @class='small-box-footer']")
        adminusertile.click()
        newbutton=self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-danger']")
        newbutton.click()
        adminusername=self.driver.find_element(By.XPATH, "//input[@id='username']")
        adminusername.send_keys("subitty s")
        adminpassword=self.driver.find_element(By.XPATH, "//input[@id='password']")
        adminpassword.send_keys("admin")
        usertype=self.driver.find_element(By.XPATH, "//select[@id='user_type']")
        select=Select(usertype)
        select.select_by_visible_text("Staff")
        savebutton=self.driver.find_element(By.XPATH, "//button[@name='Create']")
        savebutton.click()"""

        currenturl = self.driver.current_url
        assert currenturl == "https://groceryapp.uniqassosiates.com/admin/user/add"




