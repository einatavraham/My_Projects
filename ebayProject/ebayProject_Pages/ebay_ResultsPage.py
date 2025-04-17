from selenium.webdriver.common.by import By
import time
import re

class ResultsPage():

    def __init__(self, driver):
        self.driver = driver

    def checkResults_by_prices (self,minPrice_text, maxPrice_text):

        numeric_price = 0
        time.sleep(5)
        product_prices = self.driver.find_elements(By.CSS_SELECTOR, '[class="s-item__price"]')

        correct_results = 0
        incorrect_results = 0

        for price in product_prices:
            price_text = price.text
            cleaned_price = price_text.replace("ILS", "").replace(" ", "")
            if cleaned_price:
                numeric_price = int(cleaned_price[:cleaned_price.find('.')])

                if numeric_price >= int(minPrice_text) and numeric_price <= int(maxPrice_text):
                    print(f"OK - the price ", {numeric_price}, " is in the specified prices range")
                    correct_results = correct_results + 1
                else:
                    print(f"Error: ", {numeric_price}, "is out of the specified prices range")
                    incorrect_results = incorrect_results + 1
        total_results = correct_results+incorrect_results
        print()
        print ("Result Analysis")
        print ("===============")
        print (f"Out of ",{total_results}," search results", {correct_results}, " are correct and ", {incorrect_results}," are incorrect")

        assert ((incorrect_results / total_results) * 100) < 30, f"There are 30% or more wrong search results"

    def checkResults_by_keywords (self, text_to_find):

        product_titles = self.driver.find_elements(By.CSS_SELECTOR, 'div.s-item__title span')
        incorrect_results = 0
        correct_results = 0
        for title in product_titles:
            if len(title.text) != 0:
                print()
                print(title.text)

                found_text = re.search(text_to_find, title.text, flags=re.IGNORECASE)
                if found_text ==  None:
                   print("Error: incorrect search result")
                   incorrect_results = incorrect_results + 1
                else:
                   print("correct search result")
                   correct_results = correct_results + 1

        print()
        print("Result Analysis")
        print("===============")
        total_search_results = correct_results + incorrect_results
        print(f"correct results: ", {correct_results}, "incorrect results: ",{incorrect_results}, " Total: ", {total_search_results})

        assert ((incorrect_results/total_search_results)*100) < 30, f"There are 30% or more wrong search results"