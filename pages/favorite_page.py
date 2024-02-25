from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FavoritePage(BasePage):
    PRODUCT_PAGE_URL = (
        "https://www.emag.ro/robot-de-bucatarie-bosch-800-w-bol-2-3-l-2-viteze-alb-gri-mcm3100w/pd/DZ1KJYBBM/")
    ADAUGA_LA_FAVORITE_BUTTON = (By.XPATH, '//button[@class="add-to-favorites btn"]')

    FAVORITE_BUTTON = (By.CSS_SELECTOR, '#my_wishlist')
    PRODUCT = (By.XPATH, '//*[@id="list-of-favorites"]//a[@data-zone="title"]')

    def navigate_to_product_page_url(self):
        self.driver.get(self.PRODUCT_PAGE_URL)

    def click_adauga_la_favorite_button(self):
        self.click(self.ADAUGA_LA_FAVORITE_BUTTON)

    def click_favorite_button(self):
        self.click(self.FAVORITE_BUTTON)

    def is_product_displayed_favorite(self, product_name):
        product = (By.XPATH, f'//*[@title[contains(.,"{product_name}")]]')
        self.is_element_displayed(product)

    def test_url(self):
        current_url = self.driver.current_url
        assert current_url == 'https://www.emag.ro/favorites?ref=ua_favorites'
