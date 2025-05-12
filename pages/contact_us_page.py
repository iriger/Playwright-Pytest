from playwright.sync_api import Page, expect


class ContactUsPage:

    def __init__(self, page: Page):
        self.page = page

        self.__get_in_touch_title = self.page.locator('text=Get In Touch')
        self.__continue_btn = self.page.locator('[data-qa="continue-button"]')
        self.__contact_name = self.page.locator('input[data-qa="name"]')
        self.__contact_email = self.page.locator('input[data-qa="email"]')
        self.__subject = self.page.locator('input[data-qa="subject"]')
        self.__message = self.page.locator('#message')
        self.__submit_message_btn = self.page.locator('[data-qa="submit-button"]')
        self.__message_submit_success = self.page.locator('[class="status alert alert-success"]')


    def is_get_get_in_touch_title_visible(self) -> bool:
        return self.__get_in_touch_title.is_visible()

    def write_and_submit_message(self, name, email, subject, message)-> None:
        self.__contact_name.fill(name)
        self.__contact_email.fill(email)
        self.__subject.fill(subject)
        self.__message.fill(message)
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.__submit_message_btn.click()

    def is_message_submit_success_visible(self) -> bool:
        return self.__message_submit_success.is_visible()