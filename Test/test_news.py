

import pytest
from selenium.webdriver.common.by import By

from Constant import Constants
from Pages.Loginpage import Loginpage
from Pages.Newspage import Newspage
from Utilities.ExcelUtility import ExcelUtility


class Test_news:
    @pytest.mark.description("Verify user can login and return to Manage News page after clicking Home.")
    def test_news(self,browserinstance):
        self.driver=browserinstance
        self.driver.get(Constants.URL)
        self.driver.maximize_window()
        excelutility = ExcelUtility(Constants.FILEPATH)
        username = excelutility.get_string_data(2, 1, Constants.LOGINPAGE)
        password = excelutility.get_string_data(2, 2, Constants.LOGINPAGE)
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username).enter_password(password)
        homepage=loginpage.click_login()
        newspage = homepage.click_managenews().click_homebutton()
        #loginpage.enter_password(password)
        #loginpage.click_login()
        #newspage=Newspage(self.driver)
        #newspage.click_homebutton()
        self.driver.back()

        """username_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        username_textbox.send_keys(username)
        password_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_textbox.send_keys(password)
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
        managenews=self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news'and @class='small-box-footer']")
        managenews.click()
        homebutton = self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/home']")
        homebutton.click()
        self.driver.back()"""

        currenturl=self.driver.current_url
        assert currenturl == "https://groceryapp.uniqassosiates.com/admin/list-news"

    @pytest.mark.description("Verify user can login and add new news successfully.")
    def test_addnews(self,browserinstance):
        self.driver=browserinstance
        self.driver.get(Constants.URL)
        self.driver.maximize_window()
        excelutility = ExcelUtility(Constants.FILEPATH)
        username = excelutility.get_string_data(2, 1, Constants.LOGINPAGE)
        password = excelutility.get_string_data(2, 2, Constants.LOGINPAGE)
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username).enter_password(password)
        homepage=loginpage.click_login()
        newspage=homepage.click_managenews()
        #loginpage.enter_password(password)
        #loginpage.click_login()
        #newspage=Newspage(self.driver)
        newspage.click_new().enter_news("Hi selenium").click_save()
        #newspage.click_new()
        #newspage.enter_news("Hi selenium")
        #newspage.click_save()

        """username_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        username_textbox.send_keys(username)
        password_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_textbox.send_keys(password)
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
        managenews = self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news'and @class='small-box-footer']")
        managenews.click()
        new=self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-danger'] ")
        new.click()
        news=self.driver.find_element(By.XPATH,"//textarea[@id='news']")
        news.send_keys("Hi selenium")
        save=self.driver.find_element(By.XPATH,"//button[@type='submit']")
        save.click()"""

        currenturl = self.driver.current_url
        assert currenturl == "https://groceryapp.uniqassosiates.com/admin/News/add"

    @pytest.mark.description("Verify Reset Button Functionality in Manage News")
    def test_resetnews(self,browserinstance):
        self.driver=browserinstance
        self.driver.get(Constants.URL)
        self.driver.maximize_window()
        excelutility = ExcelUtility(Constants.FILEPATH)
        username = excelutility.get_string_data(2, 1, Constants.LOGINPAGE)
        password = excelutility.get_string_data(2, 2, Constants.LOGINPAGE)
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username).enter_password(password)
        homepage=loginpage.click_login()
        newspage=homepage.click_managenews().click_reset()
        #loginpage.enter_password(password)
        #loginpage.click_login()
        #newspage = Newspage(self.driver)
        #newspage.click_managenews().click_reset()
        #newspage.click_reset()

        """username_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        username_textbox.send_keys(username)
        password_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_textbox.send_keys(password)
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
        managenews = self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news'and @class='small-box-footer']")
        managenews.click()
        reset=self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-warning']")
        reset.click()"""

        currenturl = self.driver.current_url
        assert currenturl == "https://groceryapp.uniqassosiates.com/admin/list-news"

    @pytest.mark.description("Verify that user can login and open Search page and click search button successfully.")
    def test_searchnews(self, browserinstance):
        self.driver = browserinstance
        self.driver.get(Constants.URL)
        self.driver.maximize_window()
        excelutility = ExcelUtility(Constants.FILEPATH)
        username = excelutility.get_string_data(2, 1, Constants.LOGINPAGE)
        password = excelutility.get_string_data(2, 2, Constants.LOGINPAGE)
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username).enter_password(password)
        homepage=loginpage.click_login()
        newspage=homepage.click_managenews().click_search().click_searchbutton()
        #loginpage.enter_password(password)
        #loginpage.click_login()
        #newspage = Newspage(self.driver)
        #newspage.click_managenews().click_search().click_searchbutton()
        #newspage.click_search()
        #newspage.click_searchbutton()

        """username_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        username_textbox.send_keys(username)
        password_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_textbox.send_keys(password)
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
        managenews = self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news'and @class='small-box-footer']")
        managenews.click()
        search=self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        search.click()
        searchbutton=self.driver.find_element(By.XPATH,"//button[@class='btn btn-danger btn-fix']")
        searchbutton.click()"""
        currenturl = self.driver.current_url
        assert currenturl == "https://groceryapp.uniqassosiates.com/admin/news/index"














