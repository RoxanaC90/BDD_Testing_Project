from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE = 'https://auth.emag.ro/user/login'
    GREETINGS_MESSAGE = (By.CSS_SELECTOR, "h1")
    INPUT_EMAIL_LOG_IN = (By.ID, "user_login_email")
    INPUT_PASSWORD = (By.NAME, "user_login[password]")
    CONTINUE_BUTTON = (By.ID, "user_login_continue")
    LOGO = (By.XPATH, '//img[@alt="eMAG"]')
    ERROR_INVALID_EMAIL = (By.CSS_SELECTOR, 'div>div>div>form>div.form-group.has-error>div>div')
    MESSAGE_ERROR_NO_INPUT_EMAIL = (By.CSS_SELECTOR, 'body > div.auth-box.text-center > div.auth-panel > '
                                                     'div.auth-panel-body'
                                                     '> form > div.form-group.has-error > div > div')
    MESSAGE_TITLU_CONT_NOU = (By.CSS_SELECTOR, '//h1')

    """@Login1"""

    def click_continue_button(self):
        self.click(self.CONTINUE_BUTTON)

    def is_greetings_message_displayed(self):
        self.is_element_displayed(self.GREETINGS_MESSAGE)

    def get_greetings_message_text(self):
        return self.get_text(self.GREETINGS_MESSAGE)

    """@Login2"""

    def is_logo_is_displayed(self):
        self.is_element_displayed(self.LOGO)

    def get_logo_message_text(self):
        return self.get_text(self.LOGO)

    """@Login3"""

    def set_unregistred_email(self, text):
        self.type(self.INPUT_EMAIL_LOG_IN, text)

    def verify_is_message_displayed_or_not(self):
        self.verify_element_is_not_displayed_by_selector(*self.ERROR_INVALID_EMAIL)

    """@Login4"""

    def is_message_error_no_input_email_displayed(self):
        assert self.is_element_displayed(self.MESSAGE_ERROR_NO_INPUT_EMAIL)

    def get_no_mail_error_message_text(self, expected_message_text):
        actual_text = self.get_text(self.MESSAGE_ERROR_NO_INPUT_EMAIL)
        assert expected_message_text == actual_text, f"Error: message is incorrect. Expected: {expected_message_text}, actual: {actual_text}"

    """@Test_url_login_page"""

    def test_url_login_page(self):
        current_url = self.driver.current_url
        assert current_url == "https://auth.emag.ro/user/login"
