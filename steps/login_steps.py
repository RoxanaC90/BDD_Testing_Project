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


@when('The message "{greeting_message}" is displayed')
def step_impl(context, greeting_message):
    context.login_page.is_greetings_message_displayed(greeting_message)


@then('The greeting message contains "{greeting_message}" message')
def step_impl(context, greeting_message):
    context.login_page.get_greetings_message_text(greeting_message)


"""@Login2"""


@then('The Logo "{logo_text}" is displayed')
def step_impl(context, logo_text):
    context.login_page.is_logo_is_displayed(logo_text)


@then('The Logo message contains "{expected_logo_text}" message')
def step_impl(context, expected_logo_text):
    context.login_page.check_logo_message_text(expected_logo_text)


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


@then('Email error text "{error_message}" message is displayed')
def step_impl(context, error_message):
    context.login_page.is_error_no_input_email_displayed_message(error_message)


@then('Email error text contains "{message_text}" message')
def step_impl(context, message_text):
    context.login_page.check_no_mail_error_message_text(message_text)


"@Test_url_login_page"


@then('I am redirected to the Login Page https://auth.emag.ro/user/login')
def step_impl(context):
    context.login_page.test_url_login_page()
