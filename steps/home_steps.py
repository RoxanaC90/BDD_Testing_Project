from behave import *


@given('I am on the Home Page')
def step_impl(context):
    context.home_page.navigate_to_home_page()
    context.home_page.click_accept_cookies_button()
    context.home_page.click_close_intra_in_cont_button()


"""@Search1"""


@when('I click on the Search Bar')
def step_impl(context):
    context.home_page.click_search_bar()


@when('I click Search button')
def step_impl(context):
    context.home_page.click_search_button()


@then('At least 10 products are displayed')
def step_impl(context):
    context.home_page.check_product_quantity()


"""@Search2"""


@when('I search after "{product_name}"')
def step_impl(context, product_name):
    context.home_page.search_after(product_name)


@then('I verify that results contain search "{product_name}"')
def step_impl(context, product_name):
    (context.home_page.verify_results_contain_text(product_name))


"""@Filter"""


@when('I search "{searched_product}" in the Search Bar')
def step_impl(context, searched_product):
    context.home_page.search_for_products(searched_product)


@when('I click the checkbox Diagonala at 23-25 inch')
def step_impl(context):
    context.home_page.check_checkbox_diagonala()


@when('I click the checkbox Brand to LG')
def step_impl(context):
    context.home_page.check_checkbox_brand_lg()


@when('I click the checkbox Brand to Samsung')
def step_impl(context):
    context.home_page.check_checkbox_brand_samsung()


@when('I click the checkbox Pret intre 500 si 1000')
def step_impl(context):
    context.home_page.check_product_prices_checkbox()


@then('All products displayed are between 500 and 1000 lei')
def step_impl(context):
    context.home_page.check_product_prices()


"""@Test_URL"""


@when('I click on the Cart button')
def step_impl(context):
    context.home_page.click_cos_produse_page()


@then('I am redirected to the Cart Page https://www.emag.ro/cart/products?ref=cart')
def step_impl(context):
    context.home_page.test_url()


''''@Newsletter'''


@when('I set name as "{text}" in the name subscription input box')
def step_impl(context, text):
    context.home_page.set_name(text)


@when('I set email as "{text}" in the email subscription input box')
def step_impl(context, text):
    context.home_page.set_email(text)


@when('I click aboneaza-ma')
def step_impl(context):
    context.home_page.click_subscript()


@then('The error message is displayed')
def step_impl(context):
    context.home_page.is_error_message_displayed()


@then('The error message contains "{error_message}" message')
def step_impl(context, error_message):
    context.home_page.check_error_message_text(error_message)


''''@Newsletter2'''


@when('The title Abonează-te la newsletter eMAG și află de reducerile cu timp limitat! is present')
def step_impl(context):
    context.home_page.is_element_present()


@when('The title Abonează-te la newsletter eMAG și află de reducerile cu timp limitat! is displayed')
def step_impl(context):
    context.home_page.is_title_is_displayed()


@then('The title contains contains {message} message -Scenario 3')
def step_imp(context):
    context.home_page.get_title_message_text()
