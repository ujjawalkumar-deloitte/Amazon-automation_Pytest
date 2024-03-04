from selenium.webdriver.common.by import By
from test_Data.locators import log_file_path, item_to_cart
from utilities.logger import LoggerUtils
from test_Data.common_data import items_added_to_cart, cart_items
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddingToCart:

    def __init__(self, driver):
        self.driver = driver
        self.log = LoggerUtils(log_file_path)
        self.item = ""
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def add_item_to_cart(self, search):  # 3. verifying the item added in cart or not

        try:
            wait = WebDriverWait(self.driver, 10)
            self.log.log_info("Enter value in search box...")
            self.wait_for_clickable_element((By.XPATH, item_to_cart["search_box_xpath"])).clear()
            self.wait_for_clickable_element((By.XPATH, item_to_cart["search_box_xpath"])).send_keys(search)
            self.log.log_info("Clicked on search icon...")
            self.wait_for_clickable_element((By.XPATH, item_to_cart["search_icon_xpath"])).click()
            xpath_card_title = ""              # adding item in cart by searching
            search_item_xpath = {
                "tv": item_to_cart["tv_card_title_xpath1"],
                "curtains": item_to_cart["curtains_card_title_xpath2"],
                "chair": item_to_cart['chair_card_title_xpath3']
            }
            xpath_card_title = search_item_xpath.get(search)
            if xpath_card_title:
                self.item = self.wait_for_clickable_element((By.XPATH, xpath_card_title)).text
                items_added_to_cart.append(self.item)
                self.wait_for_clickable_element((By.XPATH, item_to_cart["add_to_cart"])).click()
            else:
                raise ValueError("Invalid search term")

            self.item = self.driver.find_element(By.XPATH, xpath_card_title).text
            self.wait_for_clickable_element((By.XPATH, item_to_cart["add_to_cart"])).click()
        except Exception as e:
            self.log.log_error(f"An error occurred during item addition to cart: {str(e)}")

    def verify_cart_item(self):

        try:
            self.log.log_info(f"verify_cart_item Test")
            cart_link = self.wait_for_clickable_element((By.XPATH, item_to_cart["cart_link_xpath"]))
            cart_link.click()
            # elements = self.wait_for_clickable_element((By.CSS_SELECTOR, item_to_cart["cart_elements_css"]))
            # elements = self.driver.find_elements(By.XPATH, "//ul/li/span/a/span/span/span[1]")
            # element = self.driver.find_element(By.XPATH, "(//ul/li/span/a/span/span/span[1])[1]").text
            # cart_item_xpath = '//*[@id="sc-active-6df03f90-8490-48f3-8277-00aa72e5427a"]/div[4]/div/div[3]/ul/li/span/a/span[1]/span/span[2]'
            cart_item_xpath = '//ul/li/span/a/span[1]/span/span[2]'               # verifying items added in cart or not
            elements = self.driver.find_elements(By.XPATH, cart_item_xpath)
            for item in elements:
                cart_items.append(item.text)
            self.log.log_info(f"Item added in the array Locally")

            for item in cart_items:
                self.log.log_info(f"cart_items : {item}")

            for item in items_added_to_cart:
                self.log.log_info(f"items_added_to_cart : {item}")

        except Exception as e:
            self.log.log_error(f"An error occurred during cart item verification: {str(e)}")
            assert False
