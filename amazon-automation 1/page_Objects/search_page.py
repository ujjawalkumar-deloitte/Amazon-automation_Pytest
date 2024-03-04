from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test_Data.locators import log_file_path, search_xpath
from utilities.logger import LoggerUtils


class SearchTest:

    def __init__(self, driver):
        self.driver = driver
        self.log = LoggerUtils(log_file_path)
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def search(self,search):
        try:
            wait = WebDriverWait(self.driver, 10)  # Maximum wait time of 10 seconds
            self.log.log_info("clear the search box...")
            self.wait_for_clickable_element((By.XPATH, search_xpath["search_box_xpath"])).clear()
            self.log.log_info("entering samsung keyword in search box...")
            self.wait_for_clickable_element((By.XPATH, search_xpath["search_box_xpath"])).send_keys(search)
            self.log.log_info("selecting product from search box filter...")
            self.wait_for_clickable_element((By.XPATH, search_xpath["select_product_xpath"])).click()
            self.log.log_info("clicking on the product...")
            self.wait_for_clickable_element((By.XPATH, search_xpath["click_on_product_xpath"])).click()
            self.log.log_info("switching the tab...")
            next_tab = self.driver.window_handles[1]
            self.driver.switch_to.window(next_tab)  # switch to next tab
            # self.driver.close()  # closing the current tab
            # self.driver.switch_to.window(self.driver.window_handles[0])  # Switch to the main window or the window you want to proceed with
            act_text = 'Titanium Gray'
            exp_text = self.driver.find_element(By.XPATH, search_xpath["samsung_s24_assert"]).text
            if act_text in exp_text:
                assert True
            else:
                print(f"Actual text: {act_text}")
                self.driver.save_screenshot(".\\Screenshots\\" + "search_product_title_assertion_failed_04.png")

                assert False
        except Exception as e:
            self.log.log_error(f"An error occurred: {str(e)}")
            assert False
