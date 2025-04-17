from ebayProject.ebayProject_Pages.ebay_Homepage import HomePage
from ebayProject.ebayProject_Pages.ebay_AdvancedPage import AdvancedPage
from ebayProject.ebayProject_Tests.ebay_seleniumBase import seleniumBasePage
from ebayProject.ebayProject_Pages.ebay_ResultsPage import ResultsPage
import time
from ebayProject.ebayProject_Tests.globals import PRODUCT, KEYWORD_OPTION


class searchByKeywords():
    base = seleniumBasePage()
    driver = base.selenium_start()
    ebay_home = HomePage(driver)
    ebay_advanced = AdvancedPage(driver)
    ebay_results = ResultsPage(driver)

    driver.get("https://www.ebay.com/")

    ebay_home.click_advanced()
    ebay_advanced.get_product_name(PRODUCT)
    ebay_advanced.set_advanced_Keywords_dropdown(KEYWORD_OPTION)
    ebay_advanced.click_Search_button()
    ebay_results.checkResults_by_keywords(PRODUCT)

    base.selenium_end(driver)




