from behave import *


@given('I am on the product page')
def step_impl(context):
    context.favorite_page.navigate_to_product_page_url()


@when('I click Adauga la favorite button')
def step_impl(context):
    context.favorite_page.click_adauga_la_favorite_button()


@when('I click the favourite button')
def step_impl(context):
    context.favorite_page.click_favorite_button()


@then('I verify that the product "{product_name}" is in favorite page')
def step_impl(context, product_name):
    context.favorite_page.is_product_displayed_favorite(product_name)


@then('I verify the favorite page url')
def step_impl(context):
    context.favorite_page.test_url()
