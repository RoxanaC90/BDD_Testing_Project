from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class CartPage(BasePage):
    PRODUCT_PAGE = ("https://www.emag.ro/multifunctional-inkjet-color-canon-tr4650-a4-wireless-adf-5072c006aa/pd"
                    "/DC0M3XMBM/")
    COS_DE_CUMPARATURI_PAGE = 'https://www.emag.ro/cart/products?ref=cart'
    ADAUGA_IN_COS_BUTTON = By.XPATH, ('//*[@id="main-container"]/section[3]/div/div[1]/div[2]/div/div[2]/div[2]/form['
                                      '1]/div/div[3]/div[3]/div[1]/button')
    VEZI_DETALII_COS_BUTTON = By.LINK_TEXT, 'Vezi detalii cos'
    PRODUCT = By.PARTIAL_LINK_TEXT, 'Multifunctional Inkjet color Canon TR4650, A4, Wireless , ADF'
    STERGE_COS_BUTTON = By.XPATH, '//*[@id="cart-products"]/div/div[1]/div[5]/div/div/div[2]/div[2]/div[2]/button'
    MESSAGE_STERGERE_COS = By.PARTIAL_LINK_TEXT, ('Cosul tau de cumparaturi  nu contine produse. Pentru a adauga '
                                                  'produse in cos te rugam')

    def navigate_to_product_page(self):
        self.driver.get(self.PRODUCT_PAGE)
        self.driver.maximize_window()
        sleep(2)

    def click_adauga_in_cos_button(self):
        self.click(self.ADAUGA_IN_COS_BUTTON)
        sleep(2)

    def click_vezi_detalii_cos_button(self):
        self.click(self.VEZI_DETALII_COS_BUTTON)
        sleep(2)

    def is_product_displayed(self):
        assert self.is_element_displayed(self.PRODUCT)
        sleep(2)

    def click_sterge_cos_button(self):
        self.click(self.STERGE_COS_BUTTON)
        sleep(2)

    def is_cos_de_cumparaturi_is_empty(self, MESSAGE_STERGERE_COS):
        pass

    def is_message_displayed_when_cos_de_cumparaturi_is_empty(self):
        assert self.is_cos_de_cumparaturi_is_empty(self.MESSAGE_STERGERE_COS)



