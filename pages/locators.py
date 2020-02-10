from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > a.btn-default')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_PASSWORD_FIELD_REPEAT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"].btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '.basket-mini')
    PRODUCT_ADDING_MESSAGE = (By.CSS_SELECTOR, '.alertinner > strong')
    PRODUCT_PRICE_ADDING_MESSAGE = (By.CSS_SELECTOR, '.alertinner > p > strong')

