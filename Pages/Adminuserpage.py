from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities.PageUtility import PageUtility
from Utilities.WaitUtility import WaitUtility


class Adminuserpage:
    def __init__(self, driver):
        self.driver = driver
        self.waitutility = WaitUtility()
        self.pageutility = PageUtility()
        self.newbuttonlocator=(By.XPATH, "//a[@class='btn btn-rounded btn-danger']")
        self.adminusernamelocator=(By.XPATH, "//input[@id='username']")
        self.adminpasswordlocator=(By.XPATH, "//input[@id='password']")
        self.usertypelocator=(By.XPATH, "//select[@id='user_type']")
        self.savebuttonlocator=(By.XPATH, "//button[@name='Create']")


    def click_newbutton(self):
        newbutton = self.driver.find_element(*self.newbuttonlocator)
        #newbutton = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-danger']")
        newbutton.click()
        return self
    def enter_adminusername(self,username):
        adminusername = self.driver.find_element(*self.adminusernamelocator)
        #adminusername = self.driver.find_element(By.XPATH, "//input[@id='username']")
        adminusername.send_keys(username)
        return self
    def enter_adminpassword(self,password):
        adminpassword = self.driver.find_element(*self.adminpasswordlocator)
        #adminpassword = self.driver.find_element(By.XPATH, "//input[@id='password']")
        adminpassword.send_keys(password)
        return self
    def enter_usertype(self,usertype_text):
        usertype = self.driver.find_element(*self.usertypelocator)
        self.pageutility.selectuser(usertype,usertype_text)
        #usertype = self.driver.find_element(By.XPATH, "//select[@id='user_type']")
        #select = Select(usertype)
        #select.select_by_visible_text(usertype_text)
        return self
    def click_savebutton(self):
        savebutton = self.driver.find_element(*self.savebuttonlocator)
        #savebutton = self.driver.find_element(By.XPATH, "//button[@name='Create']")
        self.waitutility.wait_until_clickable(self.driver, savebutton)
        savebutton.click()
        return self