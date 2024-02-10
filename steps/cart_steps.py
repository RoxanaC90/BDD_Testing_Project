from behave import *


@given('I am on the product page - Cart')
def step_impl(context):
    context.cart_page.navigate_to_product_page()


@when('I click on the Adauga in cos button')
def step_impl(context):
    context.cart_page.click_adauga_in_cos_button()


@when('I click on the Vezi detalii cos button')
def step_impl(context):
    context.cart_page.click_vezi_detalii_cos_button()


@then('The cart must contain Multifunctional inkjet color CANON PIXMA TR4650 product')
def step_impl(context):
    context.cart_page.is_product_displayed()


@then('I click the button Sterge')
def step_impl(context):
    context.cart_page.click_sterge_cos_button()


@then('Cosul tau de cumparaturi nu contine produse. Pentru a adauga produse in cos te rugam sa te intorci in '
      'magazin. message is displayed')
def step_impl(context):
    context.cart_page.is_cos_de_cumparaturi_is_empty('MESSAGE_STERGERE_COS')
