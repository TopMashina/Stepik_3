from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, 'div.basket-mini a.btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')
    EMAIL_FIELD = (By.ID, 'id_registration-email')
    PASS1_FIELD = (By.ID, 'id_registration-password1')
    PASS2_FIELD = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form button.btn')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main p.price_color')
    ALERT_SUCCESS = (By.CSS_SELECTOR, 'div.alert-success')


class BasketPageLocators:
    ROW_ITEMS = (By.CSS_SELECTOR, '.basket-items > div')
    BASKET_MSG = (By.CSS_SELECTOR, '#content_inner p')
