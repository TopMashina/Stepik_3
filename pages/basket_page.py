from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def rows_in_basket(self):
        return len(self.browser.find_elements(*BasketPageLocators.ROW_ITEMS))

    def is_empty_basket_message_present(self):
        return self.is_element_present(*BasketPageLocators.BASKET_MSG)
