from selenium.webdriver.common.by import By

from Pages.Adminuserpage import Adminuserpage

from Utilities.WaitUtility import WaitUtility


class Homepage:
    def __init__(self,driver):
        self.driver = driver
        self.waitutility=WaitUtility()
        self.adminlocator=(By.XPATH, "//a[@data-toggle='dropdown']")
        self.logouticonlocator=(By.XPATH, "//i[@class='ace-icon fa fa-power-off']")
        self.adminusertilelocator = (By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin'and @class='small-box-footer']")
        self.managenewslocator = (By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news'and @class='small-box-footer']")
    def click_admin(self):
        admin=self.driver.find_element(*self.adminlocator)
        #admin = self.driver.find_element(By.XPATH, "//a[@data-toggle='dropdown']")
        admin.click()
        return self
    def click_logout(self):
        from Pages.Loginpage import Loginpage
        logouticon=self.driver.find_element(*self.logouticonlocator)
        #logouticon = self.driver.find_element(By.XPATH, "//i[@class='ace-icon fa fa-power-off']")
        self.waitutility.wait_until_clickable(self.driver,logouticon)
        logouticon.click()
        return Loginpage(self.driver)

    def click_adminusertile(self):
        adminusertile = self.driver.find_element(*self.adminusertilelocator)
        # adminusertile = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin'and @class='small-box-footer']")
        adminusertile.click()
        return Adminuserpage(self.driver)
    def click_managenews(self):
        managenews=self.driver.find_element(*self.managenewslocator)
        #managenews = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news'and @class='small-box-footer']")
        managenews.click()
        from Pages.Newspage import Newspage
        return Newspage(self.driver)
