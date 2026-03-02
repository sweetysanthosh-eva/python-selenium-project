from selenium.webdriver.common.by import By


from Utilities.WaitUtility import WaitUtility


class Newspage:
    def __init__(self, driver):
        self.driver = driver
        self.waitutility = WaitUtility()
        self.managenewslocator = (By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news'and @class='small-box-footer']")
        self.homebuttonlocator=(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/home']")
        self.newlocator=(By.XPATH, "//a[@class='btn btn-rounded btn-danger']")
        self.newslocator=(By.XPATH, "//textarea[@id='news']")
        self.savelocator=(By.XPATH, "//button[@type='submit']")
        self.resetlocator=(By.XPATH, "//a[@class='btn btn-rounded btn-warning']")
        self.searchlocator=(By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        self.searchbuttonlocator=(By.XPATH, "//button[@class='btn btn-danger btn-fix']")

    def click_managenews(self):
        managenews=self.driver.find_element(*self.managenewslocator)
        #managenews = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news'and @class='small-box-footer']")
        managenews.click()
        return self


    def click_homebutton(self):
        homebutton = self.driver.find_element(*self.homebuttonlocator)
        #homebutton = self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/home']")
        homebutton.click()
        from Pages.Homepage import Homepage
        return Homepage(self.driver)

    def click_new(self):
        new = self.driver.find_element(*self.newlocator)
        #new = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-danger'] ")
        new.click()
        return self
    def enter_news(self,text):
        news = self.driver.find_element(*self.newslocator)
        #news = self.driver.find_element(By.XPATH, "//textarea[@id='news']")
        news.send_keys(text)
        return self
    def click_save(self):
        save = self.driver.find_element(*self.savelocator)
        #save = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        save.click()
        return self
    def click_reset(self):
        reset = self.driver.find_element(*self.resetlocator)
        #reset = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-warning']")
        reset.click()
        return self
    def click_search(self):
        search = self.driver.find_element(*self.searchlocator)
        #search = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        search.click()
        return self
    def click_searchbutton(self):
        searchbutton = self.driver.find_element(*self.searchbuttonlocator)
        #searchbutton = self.driver.find_element(By.XPATH, "//button[@class='btn btn-danger btn-fix']")
        self.waitutility.wait_until_clickable(self.driver,searchbutton)
        searchbutton.click()
        return self