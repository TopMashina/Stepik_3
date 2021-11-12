from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        from pages.locators import BasePageLocators
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        from pages.login_page import LoginPage
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        from pages.locators import BasePageLocators
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        from pages.locators import BasePageLocators
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented"

    def go_to_basket(self):
        from pages.locators import BasePageLocators
        self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()
        from pages.basket_page import BasketPage
        return BasketPage(browser=self.browser, url=self.browser.current_url)
