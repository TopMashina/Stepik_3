import pytest
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
