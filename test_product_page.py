import time
import string
import random
import pytest
from pages.main_page import MainPage
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage


urls_promo = [f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{x}' for x in range (0, 10)]
urls_promo[7] = pytest.param(urls_promo[7], marks=pytest.mark.xfail)

@pytest.mark.parametrize('link', urls_promo)
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()


def test_product_in_alert_matches_order(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    n, p = page.get_product_name_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.is_product_in_alert_matches(n)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS)

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS)

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    assert page.is_disappeared(*ProductPageLocators.ALERT_SUCCESS)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    login = page.go_to_login_page()
    login.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    basket = page.go_to_basket()
    assert basket.rows_in_basket() == 0
    assert basket.is_empty_basket_message_present()


def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for _ in range(str_size))


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        login_page = page.go_to_login_page()
        allowed_chars = string.ascii_letters + string.digits + string.punctuation
        login_page.register_new_user(f'{str(time.time())}@fakemail.org', random_string_generator(9, allowed_chars))

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_authorized_user()
        assert page.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS)
