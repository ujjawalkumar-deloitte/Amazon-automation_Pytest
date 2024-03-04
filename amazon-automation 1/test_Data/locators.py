
log_file_path = 'logger/automation.log'

loginXpath = {
    "sign_xpath" : "//div[@id='nav-signin-tooltip']//span[@class='nav-action-inner'][normalize-space()='Sign in']",
    "email_XPATH": "//input[@id='ap_email']",
    "email_assert_text_XPATH": "//label[@for='ap_email']",
    "continue_btn_XPATH": "//input[@id='continue']",
    "pwd_XPATH": "//input[@id='ap_password']",
    "pwd_assert_text_XPATH": "//label[@for='ap_password']",
    "sigin_btn_XPATH": "//input[@id='signInSubmit']",
    "search_dropdown_xpath": '//div[@class="nav-search-scope nav-sprite"]',
    "select_electronics_xpath": '//*[@id="searchDropdownBox"]/option[18]',
    "search_icon_xpath": "//input[@id='nav-search-submit-button']",
    "electronics_assert_xpath": "//*[@id='merchandised-search-7']/div/div/div/div[1]/h2",
    "home_page_xpath" : "//a[@id='nav-logo-sprites']"

}

item_to_cart = {
    "search_box_xpath": "//input[@id='twotabsearchtextbox']",
    "search_icon_xpath": "//input[@id='nav-search-submit-button']",
    "add_to_cart": "//*[@id='a-autoid-4-announce']",
    "cart_link_xpath" : '//span[@id="nav-cart-count"]',
    "cart_elements_css": ".sc-product-title",
    "tv_card_title_xpath1": "(//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'])[4]",
    "curtains_card_title_xpath2": "(//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'])[4]",
    "chair_card_title_xpath3": "(//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'])[4]",
    "samsung_title_xpath4":'(//*[@class="a-size-medium a-color-base a-text-normal"])[1]',
    "home_page_xpath" : "//a[@id='nav-logo-sprites']"
}
search_xpath = {
    "search_box_xpath": "//input[@id='twotabsearchtextbox']",
    "search_icon_xpath": "//input[@id='nav-search-submit-button']",
    "select_product_xpath": "//div[@aria-label='samsung s24 ultra 5g']",
    "click_on_product_xpath": "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span",
    "samsung_s24_assert": "//span[@class='selection']",
    "home_page_xpath" : "//a[@id='nav-logo-sprites']"
}
manage_address_path = {
    "your_account_id": "nav-link-accountList",
    "your_address_xpath": "//h2[normalize-space()='Your Addresses']",
    "add_address_icon_xpath": "//*[@class='a-box first-desktop-address-tile']",
    "add_address_assert": "//h2[normalize-space()='Add a new address']",
    "full_name_xpath" : "//input[@id='address-ui-widgets-enterAddressFullName']",
    "mobile_number_css" : "#address-ui-widgets-enterAddressPhoneNumber",
    "pincode_css": "#address-ui-widgets-enterAddressPostalCode",
    "house_no_css": "#address-ui-widgets-enterAddressLine1",
    "area_css" : "#address-ui-widgets-enterAddressLine2",
    "landmark_xpath" : "//input[@id='address-ui-widgets-landmark']",
    "add_address_xpath": '//input[@aria-labelledby="address-ui-widgets-form-submit-button-announce"]',
    "saved_address_assert": "//h4[normalize-space()='Address saved']",
    "home_page_xpath": "//a[@id='nav-logo-sprites']"

}

logoutXpath = {
    "element_to_hover_over": "//*[@id='nav-link-accountList-nav-line-1']",
    "manage_profile_assert": "//span[@class='sc-ksBlkl sc-jRwbcX fedVjG fqsXfW']",
    "logout_xpath": "//span[normalize-space()='Sign Out']",
    "logout_assert": "//h1[normalize-space()='Sign in']",
    "home_page_xpath": "//a[@id='nav-logo-sprites']"
}