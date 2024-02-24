from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver import Driver


class BasePage(Driver):
    def go_to(self, page):
        return self.driver.get(page)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_multiple(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        return self.find(locator).click()

    def type(self, locator, text):
        return self.find(locator).send_keys(text)

    def is_element_displayed(self, locator):
        is_product_displayed = False
        try:
            product_selector = locator
            product_element = self.find(*product_selector)
            is_product_displayed = product_element.is_displayed()

        except:
            pass
        assert is_product_displayed is True, f"Error: Element is not displayed properly"

    def get_text(self, locator):
        return self.find(locator).text

    def get_text_multiple(self, locator):
        return self.find_multiple(locator).text

    def wait_for_elem_by_selector(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))

    def wait_and_click_elem_by_selector(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((by, selector)))
        self.driver.find_element(by, selector).click()

    def click_if_present_by_selector(self, by, selector):
        elem_list = self.driver.find_elements(by, selector)
        if len(elem_list) == 1:
            self.wait_scroll_and_click_elem_by_selector(by, selector)

    def wait_scroll_and_click_elem_by_selector(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((by, selector)))
        elem = self.driver.find_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.driver.execute_script("arguments[0].click();", elem)

    def wait_and_fill_elem_by_selector(self, by, selector, text):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))
        self.driver.find_element(by, selector).send_keys(text)

    def verify_element_is_displayed_by_selector(self, by, selector):
        elem = self.driver.find_element(by, selector)
        self.assertTrue(elem.is_displayed(), 'Elem not displayed')

    def verify_element_is_displayed_as_list_by_selector(self, by, selector):
        elem_list = self.driver.find_elements(by, selector)
        self.assertEqual(len(elem_list), 1, 'Elem not displayed')

    def verify_element_is_not_displayed_by_selector(self, by, selector):
        elem_list = self.driver.find_elements(by, selector)
        self.assertEqual(len(elem_list), 0, 'Elem is incorrectly displayed')

    def verify_text_on_elem_by_selector(self, by, selector, expected_text):
        actual = self.driver.find_element(by, selector).text
        self.assertEqual(expected_text, actual, 'Text on element is incorrect')

    def select_dropdown_option_by_text(self, dropdown_locator, text):
        dropdown_element = self.find(dropdown_locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)

    def check_checkbox(self, checkbox_locator):
        checkbox_element = self.find(checkbox_locator)
        if not checkbox_element.is_selected():
            self.click(checkbox_locator)

    def current_url(self):
        return self.driver.current_url
