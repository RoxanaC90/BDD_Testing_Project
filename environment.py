from driver import Driver
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.favorite_page import FavoritePage
from pages.login_page import LoginPage


def before_all(context):
    context.browser = Driver()

    context.favorite_page = FavoritePage()
    context.home_page = HomePage()
    context.cart_page = CartPage()
    context.login_page = LoginPage()


def after_all(context):
    context.browser.close()
