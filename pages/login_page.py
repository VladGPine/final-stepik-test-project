from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, \
            'This is not a login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'register form is not presented'

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_FIELD)
        password_field_repeat = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_FIELD_REPEAT)
        registration_submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SUBMIT_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_field_repeat.send_keys(password)
        registration_submit_button.click()


