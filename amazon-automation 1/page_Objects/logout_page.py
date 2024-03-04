from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from test_Data.locators import log_file_path, logoutXpath
from utilities.logger import LoggerUtils


class LogoutTest:

    def __init__(self, driver):
        self.driver = driver
        self.log = LoggerUtils(log_file_path)

    def sign_out(self):
        try:
            wait = WebDriverWait(self.driver, 10)  # Maximum wait time of 10 seconds
            self.log.log_info("hovering on manage profile...")
            element_to_hover_over = self.driver.find_element(By.XPATH, logoutXpath['element_to_hover_over'])
            actions = ActionChains(self.driver)
            actions.move_to_element(element_to_hover_over).perform()  # hovering on the manage profile element
            element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, logoutXpath['manage_profile_assert']))
            )
            text_assert = element.text
            if text_assert == 'Manage Profiles':
                assert True
            else:
                print(f"text_assert: {text_assert}")
                self.driver.save_screenshot(".\\Screenshots\\" + "Manage_Profile_assertion_failed_07.png")
                assert False
            self.log.log_info("clicking on sign out...")
            wait.until(EC.element_to_be_clickable((By.XPATH, logoutXpath["logout_xpath"]))).click()     # clicking on signout text in website
            if self.driver.find_element(By.XPATH, logoutXpath["logout_assert"]).text == 'Sign in':
                print("Sign out assertion passed...")
                assert True
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "logout_assertion_failed_08.png")
                assert False

        except Exception as e:
            self.log.log_error(f"An error occurred: {str(e)}")
            assert False

