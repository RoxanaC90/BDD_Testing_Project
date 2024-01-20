from behave import *


@given('I am on the "Robot de bucatarie Bosch MCM3100W, 800 W, bol 2.3 l, 2 viteze, alb/ gri" page')
def step_impl(context):
    context.favorite_page.navigate_to_product_page_url()


@when('I click "Adauga la favorite" button')
def step_impl(context):
    context.favorite_page.click_adauga_la_favorite_button()


@when('I click the favourite button')
def step_impl(context):
    context.favorite_page.click_favorite_button()


@then('I verify that the product is in favorite page')
def step_impl(context):
    context.favorite_page.is_product_displayed()


@then('I verify the favorite page url')
def step_impl(context):
    assert context.favorite_page.test_url() == "https://www.emag.ro/favorites?ref=ua_favorites"
