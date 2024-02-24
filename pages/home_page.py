import re
from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class HomePage(BasePage):
    HOME_PAGE_URL = 'https://www.emag.ro/'
    CONTUL_MEU_BUTTON = (By.ID, 'my_account')
    INTRA_IN_CONT_BUTTON = (By.LINK_TEXT, '/user/login?ref=hdr_login_btn')
    SEARCH_BAR = (By.ID, 'searchboxTrigger')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#masthead > div > div > div.navbar-searchbox > div > form > '
                                      'div.input-group.searchbox-input > div.input-group-btn > '
                                      'button.btn.btn-default.searchbox-submit-button > i')
    ACCEPT_ALL_COOKIES_BUTTON = (By.XPATH, '//button[text()="Accept toate "]')
    CLOSE_INTRA_IN_CONT_BUTTON = (By.CSS_SELECTOR, 'body>div.gdpr-cookie-banner.js-gdpr-cookie-banner.pad-sep-xs.pad'
                                                   '-hrz-none.login-view.login-view-ro.show>div>button>i')
    PRODUCTS = (By.CLASS_NAME, 'card-item')
    PRODUCT_PRICES = (By.CSS_SELECTOR, 'd_grid > div:nth-child(3) > div > div > div.card-v2-content > '
                                       'div.card-v2-pricing > p.product-new-price')
    RESULTS = (By.CSS_SELECTOR, '#main-container > section.page-section.page-listing-v2 > div > '
                                'div.clearfix.pad-btm-md > div.page-container > '
                                'div.listing-panel.has-floating-listing-panel-footer > div.listing-panel-heading > '
                                'div > div.listing-page-title.js-head-title')
    CHECK_CHECKBOX_DIAGONALA = (By.XPATH, '//a[@data-name="23 - 25 inch"]')
    CHECK_CHECKBOX_BRAND_LG = (By.XPATH, '//a[@data-name="LG"]')
    CHECK_CHECKBOX_BRAND_SAMSUNG = (By.XPATH, '//a[@data-name="Samsung"]')
    CHECK_CHECKBOX_PRET = (By.XPATH, '//a[@data-name="500 - 1.000"]')
    SELECTED_PRODUCT = (By.CSS_SELECTOR, '#card_grid > div:nth-child(1) > div')
    COS_PRODUSE_PAGE = (By.ID, 'my_cart')
    PRICE_ELEMENT = (By.CSS_SELECTOR, '-container > section:nth-child(4) > div > div.row.product-main-area.mrg-btm-xs >'
                                      'div.col-sm-5.col-md-8.col-lg-8 > div > div.row.highlights-container > '
                                      'div:nth-child('
                                      '2) > form > div > div.highlight-content > '
                                      'div.product-page-pricing.product-highlight'
                                      '> div > div > div.pricing-block.has-installments > p.product-new-price')
    INPUT_NAME = (By.NAME, 'name')
    INPUT_EMAIL_NEWSLETTER = (By.NAME, 'email')
    ABONEAZAMA = (By.CSS_SELECTOR, 'div>div>div>form>div:nth-child(1)>div:nth-child(3)>button')
    EMAIL_ERROR = (
        By.CSS_SELECTOR, '#main-container > section:nth-child(5) > div > div > div > form > div:nth-child(1) > '
                         'div.form-group.col-md-4.semibold.has-error > span')
    NEWSLETTER_TITLE = (By.CSS_SELECTOR, '//h3')

    def navigate_to_home_page(self):
        self.driver.get(self.HOME_PAGE_URL)

    def click_accept_cookies_button(self):
        self.click_if_present_by_selector(*self.ACCEPT_ALL_COOKIES_BUTTON)

    def click_close_intra_in_cont_button(self):
        self.click_if_present_by_selector(*self.CLOSE_INTRA_IN_CONT_BUTTON)

    def click_contul_meu_button(self):
        self.click(self.CONTUL_MEU_BUTTON)

    def click_intra_in_contul_meu(self):
        self.click_if_present_by_selector(*self.INTRA_IN_CONT_BUTTON)

    def click_search_bar(self):
        self.click(self.SEARCH_BAR)

    def search_for_products(self, text):
        self.type(self.SEARCH_BAR, text)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    def check_product_quantity(self):
        found_products = self.find_multiple(self.PRODUCTS)
        assert len(found_products) > 10

    def check_product_prices(self):
        product_prices_text = [price.text for price in self.find_multiple(self.PRODUCT_PRICES)]
        prices_list = [re.sub(r'[^\d,]', '', item) for item in product_prices_text if item.strip()]
        prices_list_int = [int(item.split(',')[0]) for item in prices_list]
        conditions = [500 <= price <= 1000 for price in prices_list_int]
        assert all(conditions), "Nu toate prețurile sunt între 500 și 1000"

    def verify_results_contain_text(self, text):
        title_list = self.find_multiple(self.PRODUCTS)
        title = title_list[5].text.lower()
        self.assertTrue(text in title, 'Result does not contain search product')

    def insert_search_value(self, product_name):
        self.type(self.SEARCH_BAR, product_name)

    def search_after(self, product_name):
        self.type(self.SEARCH_BAR, product_name)

    """@Filter"""

    def check_checkbox_diagonala(self):
        self.check_checkbox(self.CHECK_CHECKBOX_DIAGONALA)

    def check_checkbox_brand_lg(self):
        self.check_checkbox(self.CHECK_CHECKBOX_BRAND_LG)

    def check_checkbox_brand_samsung(self):
        self.check_checkbox(self.CHECK_CHECKBOX_BRAND_SAMSUNG)

    def check_product_prices_checkbox(self):
        self.check_checkbox(self.CHECK_CHECKBOX_PRET)

    """@Test_url_cart"""

    def click_cos_produse_page(self):
        self.click(self.COS_PRODUSE_PAGE)

    def test_url(self):
        current_url = self.driver.current_url
        assert current_url == "https://www.emag.ro/cart/products?ref=cart"

    """"@Newsletter1"""

    def set_name(self, text):
        self.type(self.INPUT_NAME, text)

    def set_email(self, text):
        self.type(self.INPUT_EMAIL_NEWSLETTER, text)

    def click_subscript(self):
        self.click(self.ABONEAZAMA)

    def is_error_message_displayed(self):
        assert self.is_element_displayed(self.EMAIL_ERROR)

    def check_error_message_text(self, error_message):
        actual_message = self.get_text(self.EMAIL_ERROR)
        assert error_message == actual_message


