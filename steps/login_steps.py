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


@when('The message "Salut!" is displayed')
def step_impl(context):
    context.login_page.is_greetings_message_displayed()


@then('The greeting message contains "Salut!" message')
def step_impl(context):
    context.login_page.get_greetings_message_text()


"""@Login2"""


@when('I click on the Contul meu - Scenario 2')
def step_impl(context):
    context.home_page.click_contul_meu_button()


@when('I click on Intra in cont button - Scenario 2')
def step_impl(context):
    context.home_page.click_intra_in_contul_meu()


@then('The Logo "eMAG" is displayed')
def step_impl(context):
    context.login_page.is_logo_is_displayed()


@then('The Logo message contains "eMAG" message')
def step_impl(context):
    context.login_page.get_logo_message_text()


"""@Login3"""


@when('I click on the Contul meu - Scenario 3')
def step_impl(context):
    context.home_page.click_contul_meu_button()


@when('I click on Intra in cont button - Scenario 3')
def step_impl(context):
    context.home_page.click_intra_in_contul_meu()


@when('I insert an unregistered email in the mail input - Scenario 3')
def step_impl(context):
    context.login_page.set_unregistred_email("email_neinregistrat.yahoo.com")


@then('I click Continue button')
def step_impl(context):
    context.login_page.click_continue_button()


# @then('The main error message is displayed - Scenario 3')
# def step_impl(context):
#     context.login_page.is_error_invalid_message_displayed()
#
#
# @then('The error message contains "Email invalid" message - Scenario 3')
# def step_impl(context):
#     context.login_page.get_error_invalid_message_text()


"""@Login4"""


@when('I click on the Contul meu - Scenario 4')
def step_impl(context):
    context.home_page.click_contul_meu_button()


@when('I click on Intra in cont button - Scenario 4')
def step_impl(context):
    context.home_page.click_intra_in_contul_meu()


@when('I click on the Continue button - Scenario 4')
def step_impl(context):
    context.login_page.click_continue_button()


@then('Email error text contains message is displayed - Scenario 4')
def step_impl(context):
    context.login_page.is_message_error_no_input_email_displayed()


@then('Email error text contains "Câmp obligatoriu" message - Scenario 4')
def step_impl(context):
    context.login_page.get_no_mail_error_message_text()


"""@Login5"""


@when('I click on the Contul meu - Scenario 5')
def step_impl(context):
    context.home_page.click_contul_meu_button()


@when('I click on Intra in cont button - Scenario 5')
def step_impl(context):
    context.home_page.click_intra_in_contul_meu()


@then('I am redirected to the Login Page "https://auth.emag.ro/user/login"')
def step_impl(context):
    assert context.login_page.current_url() == "https://auth.emag.ro/user/login"
