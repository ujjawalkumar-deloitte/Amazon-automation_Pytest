import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test_Data.locators import log_file_path, manage_address_path
from utilities.logger import LoggerUtils


class AddressTest:

    def __init__(self, driver):
        self.driver = driver
        self.log = LoggerUtils(log_file_path)
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def add_address(self, full_name, mobile_number, pincode, house_no, area, landmark):
        wait = WebDriverWait(self.driver, 10)  # Maximum wait time of 10 seconds
        self.log.log_info("clicking on your account...")
        self.wait_for_clickable_element((By.ID, manage_address_path["your_account_id"])).click()
        self.log.log_info("clicking on your address...")
        self.wait_for_clickable_element((By.XPATH, manage_address_path["your_address_xpath"])).click()
        self.log.log_info("clicking on add address icon...")
        self.wait_for_clickable_element((By.XPATH, manage_address_path["add_address_icon_xpath"])).click()
        if self.driver.find_element(By.XPATH, manage_address_path["add_address_assert"]).text == 'Add a new address':
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Add_address_assertion_failed_05.png")
            assert False
        self.log.log_info("entering full_name...")
        self.wait_for_clickable_element((By.XPATH, manage_address_path["full_name_xpath"])).send_keys(full_name)
        self.log.log_info("entering on mobile number...")
        self.wait_for_clickable_element((By.CSS_SELECTOR, manage_address_path["mobile_number_css"])).send_keys(mobile_number)
        self.log.log_info("entering on pincode...")
        self.wait_for_clickable_element((By.CSS_SELECTOR, manage_address_path["pincode_css"])).send_keys(pincode)
        self.log.log_info("entering on house_no...")
        self.wait_for_clickable_element((By.CSS_SELECTOR, manage_address_path["house_no_css"])).send_keys(house_no)
        self.log.log_info("entering on area...")
        self.wait_for_clickable_element((By.CSS_SELECTOR, manage_address_path["area_css"])).send_keys(area)
        self.log.log_info("entering on landmark...")
        self.wait_for_clickable_element((By.XPATH, manage_address_path["landmark_xpath"])).send_keys(landmark)
        self.wait_for_clickable_element((By.XPATH, manage_address_path["add_address_xpath"])).click()
        act_text = 'Address saved'
        exp_text = self.driver.find_element(By.XPATH, manage_address_path["saved_address_assert"]).text
        if act_text in exp_text:
            assert True
        else:
            print(f"Actual text: {act_text}")
            self.driver.save_screenshot(".\\Screenshots\\" + "Address_saved_assertion_failed_06.png")
            assert False
