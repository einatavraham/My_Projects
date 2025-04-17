from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


class AdvancedPage():

    def __init__(self, driver):
        self.driver = driver

    def get_product_name (self, product_text):

        # user = driver.find_element(By.CSS_SELECTOR, 'input[class*="input_error"],[data-test="login-button"]')
        product = self.driver.find_element(By.CSS_SELECTOR, 'input[class*="textbox__control"]')
        product.click()
        product.send_keys(product_text)

    def set_price_range(self,minPrice_text, maxPrice_text):

        minPrice  = self.driver.find_element(By.ID, "s0-1-17-5[2]-@range-comp[]-@range-textbox[]-textbox")
        minPrice.click()
        minPrice.send_keys(minPrice_text)

        maxPrice = self.driver.find_element(By.ID, "s0-1-17-5[2]-@range-comp[]-@range-textbox[]_1-textbox")
        maxPrice.click()
        maxPrice.send_keys(maxPrice_text)

        time.sleep(3)

    def click_Search_button(self):

        searchBTN = self.driver.find_element(By.XPATH, '//button[@class="btn btn--primary"]')
        searchBTN.click()


    def set_advanced_Keywords_dropdown(self,text_to_set):

        time.sleep(3)
        search_options = self.driver.find_element(By.ID, "s0-1-17-4[0]-7[1]-_in_kw")
        search_option_as_drop_down = Select(search_options)
        search_option_as_drop_down.select_by_visible_text(text_to_set)


