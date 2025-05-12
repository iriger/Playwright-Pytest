from playwright.sync_api import Page, expect


class DeleteAccountPage:

    def __init__(self, page: Page):
        self.page = page

        self.__account_deleted_title = self.page.locator('[data-qa="account-deleted"]')
        self.__continue_btn = self.page.locator('[data-qa="continue-button"]')

    def is_account_deleted_title_visible(self) -> bool:
        return self.__account_deleted_title.is_visible()

    def continue_account_deleted(self) -> None:
        self.__continue_btn.click()