from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FavoritePage(BasePage):
    PRODUCT_PAGE_URL = ("https://www.emag.ro/robot-de-bucatarie-bosch-800-w-bol-2-3-l-2-viteze-alb-gri-mcm3100w/pd"
                        "/DZ1KJYBBM/")
    ADAUGA_LA_FAVORITE_BUTTON = By.CSS_SELECTOR, ('#main-container > section:nth-child(4) > div > '
                                                  'div.row.product-main-area.mrg-btm-xs > '
                                                  'div.col-sm-5.col-md-8.col-lg-8 >'
                                                  'div > div.row.highlights-container > div:nth-child(2) > '
                                                  'form.main-product-form > div.highlight-box > '
                                                  'div.product-highlight.product-page-actions.js-product-page-actions >'
                                                  'div.product-buy-area-wrapper > div.flex-item.hidden-xs>button>i')

    FAVORITE_BUTTON = (By.CSS_SELECTOR, '#my_wishlist')
    PRODUCT = (By.XPATH, '//*[@id="list-of-favorites"]//a[@data-zone="title"]')

    def navigate_to_product_page_url(self):
        self.driver.get(self.PRODUCT_PAGE_URL)

    def click_adauga_la_favorite_button(self):
        self.click(self.ADAUGA_LA_FAVORITE_BUTTON)

    def click_favorite_button(self):
        self.click(self.FAVORITE_BUTTON)

    def is_product_displayed(self):
        assert self.is_element_displayed(self.PRODUCT)

    def test_url(self):
        current_url = self.driver.current_url
        assert current_url == 'https://www.emag.ro/favorites?ref=ua_favorites'
