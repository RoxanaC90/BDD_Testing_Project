from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class FavoritePage(BasePage):
    PRODUCT_PAGE_URL = ("https://www.emag.ro/robot-de-bucatarie-bosch-800-w-bol-2-3-l-2-viteze-alb-gri-mcm3100w/pd"
                        "/DZ1KJYBBM/")
    ADAUGA_LA_FAVORITE_BUTTON = By.CSS_SELECTOR, ('#main-container > section:nth-child(4) > div > '
                                                  'div.row.product-main-area.mrg-btm-xs > div.col-sm-5.col-md-8.col-lg-8 > '
                                                  'div > div.row.highlights-container > div:nth-child(2) > '
                                                  'form.main-product-form > div.highlight-box > '
                                                  'div.product-highlight.product-page-actions.js-product-page-actions > '
                                                  'div.product-buy-area-wrapper > div.flex-item.hidden-xs>button>i')

    FAVORITE_BUTTON = (By.CSS_SELECTOR, '#my_wishlist')
    PRODUCT = By.XPATH, '//*[@id="list-of-favorites"]/div/div/div[2]/div[1]/h2/a/span'

    def navigate_to_product_page_url(self):
        self.driver.get(self.PRODUCT_PAGE_URL)
        self.driver.maximize_window()

        sleep(2)

    # def click_adauga_la_favorite_button(self):
    #     self.driver.find_element(self.ADAUGA_LA_FAVORITE_BUTTON).click()
    #     sleep(2)

    def click_adauga_la_favorite_button(self):
        self.click(self.ADAUGA_LA_FAVORITE_BUTTON)
        sleep(2)

    def click_favorite_button(self):
        self.click(self.FAVORITE_BUTTON)

    def is_product_displayed(self):
        assert self.is_element_displayed(self.PRODUCT)
        sleep(2)

    def test_url(self):
        current_url = self.driver.current_url
        return current_url
