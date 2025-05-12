from playwright.sync_api import Page, expect


class TeCasesPage:

    def __init__(self, page: Page):
        self.page = page

        self.__test_cases_page_title = self.page.locator('h2:has-text("Test Cases")')
        self.__continue_btn = self.page.locator('[data-qa="continue-button"]')
        self.__gender_mrs_box = self.page.locator('#id_gender2')
        self.__password_field = self.page.locator('#password')

    def is_test_cases_page_title_visible(self) -> bool:
        return self.__test_cases_page_title.is_visible()
