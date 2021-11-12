import math
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def open_basket(self):
        self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()

    def get_product_name_price(self):
        n = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        p = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return n, p

    def is_product_in_alert_matches(self, name):
        el = self.browser.find_elements(*ProductPageLocators.ALERT_SUCCESS)
        for x in el:
            if len(x.find_elements(By.XPATH, f'//*[contains(text(), "{name}")]')) > 0:
                return True
        return False
