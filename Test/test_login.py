import pytest
from selenium.webdriver.common.by import By

from Constant import Constants
from Pages.Loginpage import Loginpage
from Utilities.ExcelUtility import ExcelUtility


class Test_login:
    @pytest.mark.run(order=1)
    @pytest.mark.description("login with valid credentials")
    @pytest.mark.smoke
    def test_loginwithvalidcred(self,browserinstance):
        self.driver=browserinstance
        self.driver.get(Constants.URL)
        self.driver.maximize_window()
        excelutility=ExcelUtility(Constants.FILEPATH)
        username=excelutility.get_string_data(2,1,Constants.LOGINPAGE)
        password=excelutility.get_string_data(2,2,Constants.LOGINPAGE)
        loginpage=Loginpage(self.driver)
        loginpage.enter_username(username).enter_password(password)
        homepage=loginpage.click_login()


        """username_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        username_textbox.send_keys(username)
        password_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_textbox.send_keys(password)
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()"""

        #using assertion to check the expected result is met
        currenturl=self.driver.current_url
        assert currenturl=="https://groceryapp.uniqassosiates.com/admin"

        # 2 login with invalid username and valid password

    @pytest.mark.run(order=2)
    @pytest.mark.description("login with invalid username and valid password ")
    def test_loginwithinvalidusername(self, browserinstance):
        self.driver = browserinstance
        self.driver.get(Constants.URL)
        self.driver.maximize_window()
        excelutility = ExcelUtility(Constants.FILEPATH)
        username = excelutility.get_string_data(4, 1, Constants.LOGINPAGE)
        password = excelutility.get_string_data(4, 2, Constants.LOGINPAGE)
        loginpage = Loginpage(self.driver)
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username).enter_password(password).click_login()
        #loginpage.enter_password(password)
        #loginpage.click_login()

        """username_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        username_textbox.send_keys(username)
        password_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_textbox.send_keys(password)
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()"""

        currenturl = self.driver.current_url
        assert currenturl == "https://groceryapp.uniqassosiates.com/admin/login"

        # 3 login with invalid password and valid username

    @pytest.mark.run(order=3)
    @pytest.mark.description("login with valid username and invalid password ")
    def test_loginwithinvalidpassword(self, browserinstance):
        self.driver = browserinstance
        self.driver.get(Constants.URL)
        self.driver.maximize_window()
        excelutility = ExcelUtility(Constants.FILEPATH)
        username = excelutility.get_string_data(3, 1, Constants.LOGINPAGE)
        password = excelutility.get_string_data(3, 2, Constants.LOGINPAGE)
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username).enter_password(password).click_login()
        #loginpage.enter_password(password)
        #loginpage.click_login()

        """username_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        username_textbox.send_keys(username)
        password_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_textbox.send_keys(password)
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()"""

        currenturl = self.driver.current_url
        assert currenturl == "https://groceryapp.uniqassosiates.com/admin/login"


         # 4 login with invalid credentials

    @pytest.mark.run(order=4)
    @pytest.mark.description("login with invalid credentials")
    @pytest.mark.parametrize("username",["user1","test1","data1"]) #to execute multiple data for same test case
    def test_loginwithinvalidcred(self,browserinstance,username):
        self.driver=browserinstance
        self.driver.get(Constants.URL)
        self.driver.maximize_window()
        excelutility = ExcelUtility(Constants.FILEPATH)
        username = excelutility.get_string_data(5, 1, Constants.LOGINPAGE)
        password = excelutility.get_string_data(5, 2, Constants.LOGINPAGE)
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username).enter_password(password).click_login()
        #loginpage.enter_password(password)
        #loginpage.click_login()

        """username_textbox=self.driver.find_element(By.XPATH,"//input[@placeholder='Username']")
        username_textbox.send_keys(username)
        password_textbox=self.driver.find_element(By.XPATH,"//input[@placeholder='Password']")
        password_textbox.send_keys(password)
        button=self.driver.find_element(By.XPATH,"//button[@type='submit']")
        button.click()"""

        currenturl = self.driver.current_url
        assert currenturl == "https://groceryapp.uniqassosiates.com/admin/login"






