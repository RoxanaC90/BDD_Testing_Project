from behave import *
from pages.home_page import HomePage


@given('I am on the Home Page')
def step_impl(context):
    # context.home_page = HomePage()
    context.home_page.navigate_to_home_page()
    context.home_page.click_accept_cookies_button()
    context.home_page.click_close_intra_in_cont_button()


"""@Search1"""


@when('I click on the Search Bar')
def step_impl(context):
    context.home_page.click_search_bar()


@when('I search ”Monitoare Gaming” in the Search Bar')
def step_impl(context):
    context.home_page.search_for_products("Monitoare Gaming")


@when('I click Search button')
def step_impl(context):
    context.home_page.click_search_button()


@then('At least 10 products are displayed')
def step_impl(context):
    # product_quantity = context.driver.find_element(By.XPATH,
    #                                                '//*[@id="main-container"]/section[1]/div/div[3]/div[2]/div['
    #                                                '1]/div[1]/div/span')
    # products_int = int(product_quantity.get_attribute('945'))
    # assert products_int >= 10
    assert context.home_page.check_product_quantity() >= 10


"""@Filter"""


@when('I click on the Search bar- Scenario 2')
def step_impl(context):
    context.home_page.click_search_bar()


@when('I search ”Monitoare Gaming” in the Search Bar- Scenario 2')
def step_impl(context):
    context.home_page.search_for_products("Monitoare Gaming")


@when('I click Search button - Scenario 2')
def step_impl(context):
    context.home_page.click_search_button()


@when('I click the checkbox "Diagonala" at "23-25 inch"')
def step_impl(context):
    context.home_page.check_checkbox_diagonala()


@when('I click the checkbox "Brand" to LG')
def step_impl(context):
    context.home_page.check_checkbox_brand_lg()


@when('I click the checkbox "Brand" to Samsung')
def step_impl(context):
    context.home_page.check_checkbox_brand_samsung()


@when('I click the checkbox "Pret" intre 500 si 1000')
def step_impl(context):
    context.home_page.check_product_prices_checkbox()


@then('All products displayed are between 500 and 1000 lei')
def step_impl(context):
    for price in context.home_page.check_product_prices():
        assert 500 <= price <= 1000


@then('I click the selected product "Monitor gaming, Samsung, Odyssey S24AG300, 24&quot;, Full HD, 1 ms, 144 Hz, '
      'Freesync Premium, Design ergonomic, HDMI, Negru"')
def step_impl(context):
    context.home_page.click_the_selectd_product()


"""@Test_URL"""


@when('I click on the Cart button')
def step_impl(context):
    context.home_page.click_cos_produse_page()


@then('I am redirected to the Cart Page "https://www.emag.ro/cart/products?ref=cart"')
def step_impl(context):
    assert context.home_page.test_url() == "https://www.emag.ro/cart/products?ref=cart"


''''@Newsletter'''


@when('I set name as {text}')
def step_impl(context, text):
    context.home_page.set_name(text)


@when('I set email as {text}')
def step_impl(context, text):
    context.home_page.set_email(text)


@when('I click aboneaza-ma')
def step_impl(context):
    context.home_page.click_subscript()


@then('The error message is displayed')
def step_impl(context):
    context.home_page.is_error_message_displayed()


@then('The error message contains "Email incorect" message')
def step_impl(context):
    context.home_page.get_error_message_text()


''''@Newsletter2'''


@when('The title "Abonează-te la newsletter eMAG și află de reducerile cu timp limitat!" is present')
def step_impl(context):
    context.home_page.is_element_present()


@when('The title "Abonează-te la newsletter eMAG și află de reducerile cu timp limitat!" is displayed')
def step_impl(context):
    context.home_page.is_title_is_displayed()


@then('The title contains contains {message} message -Scenario 3')
def step_imp(context):
    context.home_page.get_title_message_text()
