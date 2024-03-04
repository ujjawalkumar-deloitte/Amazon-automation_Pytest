from page_Objects.add_address_page import AddressTest
from page_Objects.cart_page import AddingToCart
from page_Objects.login_page import LoginTest
from page_Objects.logout_page import LogoutTest
from page_Objects.search_page import SearchTest
from utilities.read_excel import read_excel
from test_Data.common_data import xlsx_path



class TestCases:
    # def test_open_website(self, setup):
    #     self.driver = setup
    #     self.driver.maximize_window()

    def test_login_page(self, setup):
        self.baseURL, self.email, self.password = read_excel(xlsx_path, 1)
        self.login = LoginTest(setup)
        self.login.sign_in(self.baseURL, self.email, self.password)

    def test_addto_cart(self, setup):
        self.search = read_excel(xlsx_path, 3)
        self.cart_page = AddingToCart(setup)
        for i in self.search:
            if i == "curtains":
                self.cart_page.add_item_to_cart(i)
            elif i == "tv":
                self.cart_page.add_item_to_cart(i)
            elif i == "chair":
                self.cart_page.add_item_to_cart(i)
        self.cart_page.verify_cart_item()

    def test_search_keyword(self, setup):
        self.search = read_excel(xlsx_path, 5)
        self.search_obj = SearchTest(setup)
        self.search_obj.search(self.search)

    def test_add_address(self, setup):
        self.full_name, self.mobile_number, self.pincode, self.house_no, self.area, self.landmark = read_excel(xlsx_path, 4)
        self.manage_address = AddressTest(setup)
        self.manage_address.add_address(self.full_name, self.mobile_number, self.pincode, self.house_no, self.area, self.landmark)

    def test_logout(self, setup):
        self.logout = LogoutTest(setup)
        self.logout.sign_out()
