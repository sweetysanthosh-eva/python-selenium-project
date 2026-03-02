from selenium.webdriver.common.by import By


from Utilities.WaitUtility import WaitUtility


class Loginpage:
    def __init__(self, driver):
        self.driver = driver
        self.waitutility = WaitUtility()
        self.usernamelocator=(By.XPATH, "//input[@placeholder='Username']")
        self.passwordlocator=(By.XPATH, "//input[@placeholder='Password']")
        self.buttonlocator=(By.XPATH, "//button[@type='submit']")
    def enter_username(self, username):
        usernamefield=self.driver.find_element(*self.usernamelocator)
        #username_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        usernamefield.send_keys(username)
        return self
    def enter_password(self, password):
        passwordfield=self.driver.find_element(*self.passwordlocator)
        #password_textbox = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        passwordfield.send_keys(password)
        return self
    def click_login(self):
        button=self.driver.find_element(*self.buttonlocator)
        #button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        self.waitutility.wait_until_clickable(self.driver, button)
        button.click()
        from Pages.Homepage import Homepage
        return Homepage(self.driver)


