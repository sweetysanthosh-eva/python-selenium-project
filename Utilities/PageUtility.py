from selenium.webdriver.support.select import Select


class PageUtility:
    def selectuser(self,usertype,text):
        select = Select(usertype)
        select.select_by_visible_text(text)