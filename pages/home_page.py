from playwright.sync_api import Page, expect


class HomePage:

    def __init__(self, page: Page):
        self.page = page

        self.__home_main_section = self.page.locator('.col-sm-12')
        self.__signup_login_btn = self.page.locator('a[href="/login"]')
        self.__loggedin_as = self.page.locator('.fa.fa-user')
        self.__delete_account_btn = self.page.locator('[href="/delete_account"]')
        self.__logout_btn = self.page.locator('a[href="/logout"]')
        self.__contact_us_btn = self.page.locator('a[href="/contact_us"]')
        self.__home_btn = self.page.locator('li>[href="/"]')
        self.__test_cases_btn = self.page.locator('li>[href="/test_cases"]')
        self.__products_btn = self.page.locator('a[href="/products"]')
        self.__footer = self.page.locator('#footer')
        self.__subscription_title = self.page.locator('text=Subscription')
        self.__subscription_email_field = self.page.locator('#susbscribe_email')
        self.__subscribe_btn = self.page.locator('#subscribe')
        self.__subscribe_success_message = self.page.locator('#success-subscribe')

    def is_main_section_visible(self) -> bool:
        return self.__home_main_section.is_visible()

    def go_to_signup_page (self) -> None:
        self.__signup_login_btn.click()

    def is_loggedin_as_visible(self) -> bool:
        return self.__loggedin_as.is_visible()

    def delete_account(self) -> None:
        self.__delete_account_btn.click()

    def logout(self) -> None:
        self.__logout_btn.click()

    def goto_contact_us(self) -> None:
        self.__contact_us_btn.click()

    def goto_home(self) -> None:
        self.__home_btn.click()

    def goto_test_cases_page(self) -> None:
        self.__test_cases_btn.click()

    def goto_products_page(self) -> None:
        self.__products_btn.click()

    def goto_footer(self) -> None:
        self.__footer.scroll_into_view_if_needed()

    def is_subscription_title_visible(self) -> bool:
        return self.__subscription_title.is_visible()

    def subscribe(self, subscription_email) -> None:
        self.__subscription_email_field.fill(subscription_email)
        self.__subscribe_btn.click()

    def is_subscription_success_message_visible(self) -> bool:
        return self.__subscribe_success_message.is_visible()
