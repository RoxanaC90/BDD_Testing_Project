import re
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class HomePage(BasePage):
    HOME_PAGE_URL = 'https://www.emag.ro/'
    CONTUL_MEU_BUTTON = (By.ID, 'my_account')
    INTRA_IN_CONT_BUTTON = (By.LINK_TEXT, '/user/login?ref=hdr_login_btn')
    SEARCH_BAR = (By.ID, 'searchboxTrigger')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="masthead"]/div/div/div[2]/div/form/div[1]/div[2]/button[2]/i')
    ACCEPT_ALL_COOKIES_BUTTON = (By.XPATH, '//button[text()="Accept toate "]')
    CLOSE_INTRA_IN_CONT_BUTTON = (By.CSS_SELECTOR, 'body>div.gdpr-cookie-banner.js-gdpr-cookie-banner.pad-sep-xs.pad'
                                                   '-hrz-none.login-view.login-view-ro.show>div>button>i')
    PRODUCTS = (By.CLASS_NAME, 'card-item')
    PRODUCT_PRICES = (By.XPATH, '//*[@id="card_grid"]/div[3]/div/div/div[4]/div[1]/p[2]')
    RESULTS = (By.XPATH, '//*[@id="main-container"]/section[1]/div/div[3]/div[2]/div[1]/div[1]/div/span')
    CHECK_CHECKBOX_DIAGONALA = (By.XPATH, '//*[@id="js-filter-6535-collapse"]/div/a[4]')
    CHECK_CHECKBOX_BRAND_LG = (By.XPATH, '// *[ @ id = "js-filter-6415-collapse"]/div[2]/a[6]')
    CHECK_CHECKBOX_BRAND_SAMSUNG = (By.XPATH, '//*[@id="js-filter-6415-collapse"]/div[2]/a[8]')
    CHECK_CHECKBOX_PRET = (By.XPATH, '//*[@id="js-filter-6411-collapse"]/div[1]/a[2]')
    SELECTED_PRODUCT = (By.XPATH, '//*[@id="card_grid"]/div[1]/div/div/div[3]/a')
    COS_PRODUSE_PAGE = (By.ID, 'my_cart')
    PRICE_ELEMENT = (By.XPATH, '//*[@id="main-container"]/section[3]/div/div[1]/div[2]/div/div[2]/div['
                               '2]/form/div/div[1]/div[1]/div/div/div[1]/p[2]')
    INPUT_NAME = (By.NAME, 'name')
    INPUT_EMAIL_NEWSLETTER = (By.NAME, 'email')
    ABONEAZAMA = (By.CSS_SELECTOR, 'div>div>div>form>div:nth-child(1)>div:nth-child(3)>button')
    EMAIL_ERROR = (By.XPATH, '//*[@id="main-container"]/section[3]/div/div/div/form/div[1]/div[2]/span')
    NEWSLETTER_TITLE = By.CSS_SELECTOR, '//h3'

    def navigate_to_home_page(self):
        self.driver.get(self.HOME_PAGE_URL)
        self.driver.maximize_window()
        sleep(2)

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
        sleep(2)

    def search_for_products(self, text):
        self.type(self.SEARCH_BAR, text)
        sleep(2)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)
        sleep(10)

    def click_the_selected_product(self):
        self.click(self.SELECTED_PRODUCT)
        sleep(2)

    def check_product_quantity(self):
        found_products = self.find_multiple(self.PRODUCTS)
        return len(found_products)

    def check_product_prices(self):
        product_prices_text = [price.text for price in self.find_multiple(self.PRODUCT_PRICES)]
        prices_list = [re.sub(r'[^\d,]', '', item) for item in product_prices_text if item.strip()]
        prices_list_int = [int(item.split(',')[0]) for item in prices_list]
        return prices_list_int

    """@Filter"""

    def check_checkbox_diagonala(self):
        self.check_checkbox(self.CHECK_CHECKBOX_DIAGONALA)
        sleep(2)

    def check_checkbox_brand_lg(self):
        self.check_checkbox(self.CHECK_CHECKBOX_BRAND_LG)
        sleep(2)

    def check_checkbox_brand_samsung(self):
        self.check_checkbox(self.CHECK_CHECKBOX_BRAND_SAMSUNG)
        sleep(2)

    def check_product_prices_checkbox(self):
        self.check_checkbox(self.CHECK_CHECKBOX_PRET)
        sleep(2)

    """@Test_url_cart"""

    def click_cos_produse_page(self):
        self.click(self.COS_PRODUSE_PAGE)
        sleep(2)

    def test_url(self):
        current_url = self.driver.current_url
        return current_url

    """"@Newsletter1"""

    def set_name(self, text):
        self.type(self.INPUT_NAME, text)

    def set_email(self, text):
        self.type(self.INPUT_EMAIL_NEWSLETTER, text)

    def click_subscript(self):
        self.click(self.ABONEAZAMA)
        sleep(2)

    def is_error_message_displayed(self):
        assert self.is_element_displayed(self.EMAIL_ERROR)

    def get_error_message_text(self):
        return self.get_text(self.EMAIL_ERROR)

    def click_the_selectd_product(self):
        self.wait_scroll_and_click_elem_by_selector(*self.SELECTED_PRODUCT)


