from playwright.sync_api import Page, expect


class AccountCreatedPage:

    def __init__(self, page: Page):
        self.page = page

        self.__account_created_title = self.page.locator('[data-qa="account-created"]')
        self.__continue_btn = self.page.locator('[data-qa="continue-button"]')
        self.__gender_mrs_box = self.page.locator('#id_gender2')
        self.__password_field = self.page.locator('#password')

    def is_account_created_title_visible(self) -> bool:
        return self.__account_created_title.is_visible()

    def continue_account_created(self) -> None:
            self.__continue_btn.click()

