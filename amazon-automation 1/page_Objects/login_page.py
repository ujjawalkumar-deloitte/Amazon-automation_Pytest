from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import LoggerUtils
from selenium.webdriver.common.by import By
from test_Data.locators import loginXpath, log_file_path

class LoginTest:

    def __init__(self, driver):
        self.driver = driver
        self.log = LoggerUtils(log_file_path)
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))


    def sign_in(self, url, email, password):  # login to the website
        try:
            self.log.log_info("Site getting launched...")
            self.driver.get(url)
            self.log.log_info("Clicking on sign in...")
            wait = WebDriverWait(self.driver, 10)  # Maximum wait time of 10 seconds
            self.wait_for_visible_element((By.XPATH, loginXpath["sign_xpath"])).click()  # clicking on signin
            self.log.log_info("Entering the mobile number...")
            self.wait_for_clickable_element((By.XPATH, loginXpath["email_XPATH"])).send_keys(email)  # entering email/mobile number
            if self.driver.find_element(By.XPATH, loginXpath["email_assert_text_XPATH"]).text == 'Email or mobile phone number':
                print("1st Assertion Passed...")
                assert True
            else:
                print("1st Assertion failed...")
                self.driver.save_screenshot(".\\Screenshots\\" + "Entering_email_or mobile_number_assertion_failed_01.png")
                assert False
            self.log.log_info("Clicking on continue button...")
            self.wait_for_clickable_element((By.XPATH, loginXpath["continue_btn_XPATH"])).click()
            if self.driver.find_element(By.XPATH, loginXpath["pwd_assert_text_XPATH"]).text == 'Password':
                print("2nd Assertion passed...")
                assert True
            else:
                print("2nd Assertion failed...")
                self.driver.save_screenshot(".\\Screenshots\\" + "Password_text_assertion_failed_02.png")
            self.log.log_info("Entering the password...")
            self.wait_for_clickable_element((By.XPATH, loginXpath["pwd_XPATH"])).send_keys(password)  # entering password
            self.log.log_info("Clicking on sign in button...")
            self.wait_for_clickable_element((By.XPATH, loginXpath["sigin_btn_XPATH"])).click()
            self.log.log_info("Clicking on search box dropdown...")
            self.wait_for_clickable_element((By.XPATH, loginXpath["search_dropdown_xpath"])).click()
            self.log.log_info("Clicking on Electronics...")
            self.wait_for_clickable_element((By.XPATH, loginXpath["select_electronics_xpath"])).click()
            self.log.log_info("Clicking on search box search icon...")
            self.wait_for_clickable_element((By.XPATH, loginXpath["search_icon_xpath"])).click()
            act_text = "Electronic Devices"
            exp_text = self.driver.find_element(By.XPATH, loginXpath["electronics_assert_xpath"]).text
            print(exp_text)
            if act_text in exp_text:
                print(exp_text)
                self.driver.find_element(By.XPATH, loginXpath["home_page_xpath"]).click()
                assert True
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "Electronics_page_assertion_failed_03.png")
                assert False


        except Exception as e:
            self.log.log_error(f"An error occurred: {str(e)}")
            assert False
