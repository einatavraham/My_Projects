from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver

    def click_advanced(self):

        self.driver.find_element(By.CLASS_NAME, "gh-search-button__advanced-link").click()
