from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class LoginPage(BasePage):
    GREETINGS_MESSAGE = (By.CSS_SELECTOR, "h1")
    INPUT_EMAIL_LOG_IN = (By.ID, "user_login_email")
    INPUT_PASSWORD = (By.NAME, "user_login[password]")
    CONTINUE_BUTTON = (By.ID, "user_login_continue")
    LOGO = (By.XPATH, '/html/body/div[1]/div[1]/a/img')
    ERROR_INVALID_EMAIL = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/form/div[3]/div')
    MESSAGE_ERROR_NO_INPUT_EMAIL = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/form/div[3]/div/div')
    MESSAGE_TITLU_CONT_NOU = (By.CSS_SELECTOR, '//h1')

    """@Login1"""

    def click_continue_button(self):
        self.click(self.CONTINUE_BUTTON)

    def is_greetings_message_displayed(self):
        assert self.is_element_displayed(self.GREETINGS_MESSAGE)

    def get_greetings_message_text(self):
        return self.get_text(self.GREETINGS_MESSAGE)

    """@Login2"""

    def is_logo_is_displayed(self):
        assert self.is_element_displayed(self.LOGO)

    def get_logo_message_text(self):
        return self.get_text(self.LOGO)

    """@Login3"""

    def set_unregistred_email(self, text):
        self.type(self.INPUT_EMAIL_LOG_IN, text)

    """@Login4"""

    def is_message_error_no_input_email_displayed(self):
        assert self.is_element_displayed(self.MESSAGE_ERROR_NO_INPUT_EMAIL)

    def get_no_mail_error_message_text(self):
        return self.get_text(self.MESSAGE_ERROR_NO_INPUT_EMAIL)

    """@Login5"""

    def test_login_page_url(self):
        login_page_url = self.login_page
        return login_page_url
