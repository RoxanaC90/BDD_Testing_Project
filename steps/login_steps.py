from behave import *

"""@Login1"""


@given('I am on the Home Page going to Login Page')
def step_impl(context):
    context.home_page.navigate_to_home_page()
    context.home_page.click_accept_cookies_button()
    context.home_page.click_close_intra_in_cont_button()


@when('I click on the Contul meu')
def step_impl(context):
    context.home_page.click_contul_meu_button()


@when('I click on Intra in cont button')
def step_impl(context):
    context.home_page.click_intra_in_contul_meu()


@when('The message Salut! is displayed')
def step_impl(context):
    context.login_page.is_greetings_message_displayed()


@then('The greeting message contains Salut! message')
def step_impl(context):
    context.login_page.get_greetings_message_text()


"""@Login2"""


@then('The Logo eMAG is displayed')
def step_impl(context):
    context.login_page.is_logo_is_displayed()


@then('The Logo message contains eMAG message')
def step_impl(context):
    context.login_page.get_logo_message_text()


"""@Login3"""


@when('I insert an unregistered email in the mail input')
def step_impl(context):
    context.login_page.set_unregistred_email("email_neinregistrat.yahoo.com")


@when('I click Continue button')
def step_impl(context):
    context.login_page.click_continue_button()


@then('The error meesage is displayed')
def step_impl(context):
    context.login_page.verify_is_message_displayed_or_not()


"""@Login4"""


@when('I click on the Continue button')
def step_impl(context):
    context.login_page.click_continue_button()


@then('Email error text contains message is displayed')
def step_impl(context):
    context.login_page.is_message_error_no_input_email_displayed()


@then('Email error text contains "{message_text}" message')
def step_impl(context, message_text):
    context.login_page.get_no_mail_error_message_text(message_text)


"""@Login5"""


@then('I am redirected to the Login Page https://auth.emag.ro/user/login')
def step_impl(context):
    context.login_page.test_url_login_page()
