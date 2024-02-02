from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class CartPage(BasePage):
    PRODUCT_PAGE = ("https://www.emag.ro/multifunctional-inkjet-color-canon-tr4650-a4-wireless-adf-5072c006aa/pd"
                    "/DC0M3XMBM/")
    COS_DE_CUMPARATURI_PAGE = 'https://www.emag.ro/cart/products?ref=cart'
    ADAUGA_IN_COS_BUTTON = By.XPATH, ('//button[@type="submit" and @class="btn btn-xl btn-primary btn-emag btn-block '
                                      'main-button gtm_680klw yeahIWantThisProduct"]')
    VEZI_DETALII_COS_BUTTON = By.LINK_TEXT, 'Vezi detalii cos'
    PRODUCT = By.PARTIAL_LINK_TEXT, 'Multifunctional Inkjet color Canon TR4650, A4, Wireless , ADF'
    STERGE_COS_BUTTON = By.CSS_SELECTOR, ('#cart-products > div > div.col-md-8.col-lg-9.main-container-left > '
                                          'div.placeholder.vendors-container > div > div > div.cart-widget.cart-line '
                                          '> div.line-item.line-item-footer.hidden-xs.hidden-sm > '
                                          'div.line-footer-action-buttons > button')
    MESSAGE_STERGERE_COS = By.PARTIAL_LINK_TEXT, ('Cosul tau de cumparaturi  nu contine produse. Pentru a adauga '
                                                  'produse in cos te rugam')

    def navigate_to_product_page(self):
        self.driver.get(self.PRODUCT_PAGE)

    def click_adauga_in_cos_button(self):
        self.click(self.ADAUGA_IN_COS_BUTTON)

    def click_vezi_detalii_cos_button(self):
        self.click(self.VEZI_DETALII_COS_BUTTON)

    def is_product_displayed(self):
        assert self.is_element_displayed(self.PRODUCT)

    def click_sterge_cos_button(self):
        self.click(self.STERGE_COS_BUTTON)

    def is_cos_de_cumparaturi_is_empty(self, MESSAGE_STERGERE_COS):
        pass

    def is_message_displayed_when_cos_de_cumparaturi_is_empty(self):
        assert self.is_cos_de_cumparaturi_is_empty(self.MESSAGE_STERGERE_COS)
