from playwright.sync_api import Page, expect


class SignupLoginPage:

    def __init__(self, page: Page):
        self.page = page
        # form

        self.__signup_title = self.page.locator('text=New User Signup!')
        self.__signup_form = self.page.locator('.signup-form')
        self.__login_form = self.page.locator('.login-form')
        self.__name_input = self.page.locator('input[data-qa="signup-name"]')
        self.__email_input = self.page.locator('input[data-qa="signup-email"]')
        self.__signup_btn = self.page.locator('[data-qa="signup-button"]')
        self.__enter_account_info = self.page.locator('.login-form')
        self.__login_email = self.page.locator('[data-qa="login-email"]')
        self.__login_password = self.page.locator('[data-qa="login-password"]')
        self.__login_btn = self.page.locator('[data-qa="login-button"]')
        self.__login_error_message = self.page.locator('p[style="color: red;"]')
        self.__signup_error_message = self.page.locator('text=Email Address already exist!')


    def is_signup_title_visible(self) -> bool:
        return self.__signup_title.is_visible()


    def signup(self, name, email) -> None:
            self.__name_input.fill(name)
            self.__email_input.fill(email)
            self.__signup_btn.click()

    def is_login_form_visible(self) -> bool:
        return self.__login_form.is_visible()

    def login(self, valid_email, valid_password) -> None:
            self.__login_email.fill(valid_email)
            self.__login_password.fill(valid_password)
            self.__login_btn.click()

    def is_login_error_message_visible(self) -> bool:
        return self.__login_error_message.is_visible()

    def is_signup_error_message_visible(self) -> bool:
        return self.__signup_error_message .is_visible()