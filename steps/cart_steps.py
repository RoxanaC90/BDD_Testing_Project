from behave import *



@when('I click on the Adauga in cos button')
def step_impl(context):
    context.cart_page.click_adauga_in_cos_button()


@when('I click on the Vezi detalii cos button')
def step_impl(context):
    context.cart_page.click_vezi_detalii_cos_button()


@then('The cart must contain "{product_name}" product')
def step_impl(context, product_name):
    context.cart_page.is_element_displayed(product_name)


@then('I click the button Sterge')
def step_impl(context):
    context.cart_page.click_sterge_cos_button()


@then('"{empty_cart_error_message}" message is displayed')
def step_impl(context, empty_cart_error_message):
    context.cart_page.is_cos_de_cumparaturi_is_empty(empty_cart_error_message)
