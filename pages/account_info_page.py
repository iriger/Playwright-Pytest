from playwright.sync_api import Page, expect


class AccountInfoPage:

    def __init__(self, page: Page):
        self.page = page

        self.__account_info_title = self.page.locator('text=Enter Account Information')
        self.__gender_mr_box = self.page.locator('#id_gender1')
        self.__gender_mrs_box = self.page.locator('#id_gender2')
        self.__password_field = self.page.locator('#password')
        self.__days_dropdown = self.page.locator('#days')
        self.__days_option = self.page.locator('#days>option[value="7"]')
        self.__months_dropdown = self.page.locator('#months')
        self.__months_option = self.page.locator('#months>option[value="5"]')
        self.__year_dropdown = self.page.locator('#years')
        self.__year_option = self.page.locator('option[value="2000"]')
        self.__newsletter_checkbox = self.page.locator('#newsletter')
        self.__specoffer_checkbox = self.page.locator('#optin')
        self.__first_name = self.page.locator('#first_name')
        self.__last_name = self.page.locator('#last_name')
        self.__company_name = self.page.locator('#company')
        self.__address_one = self.page.locator('#address1')
        self.__address_two = self.page.locator('#address2')
        self.__enter_account_info = self.page.locator('.login-form')
        self.__state = self.page.locator('#state')
        self.__city = self.page.locator('#city')
        self.__zip_code = self.page.locator('#zipcode')
        self.__mobile_number = self.page.locator('#mobile_number')
        self.__create_account_btn = self.page.locator('[data-qa="create-account"]')

    def is_account_info_title_visible(self) -> bool:
        return self.__account_info_title.is_visible()

    def fill_account_info_form (self, password, first_name, last_name, company, address_one, address_two, state, city, zip_code, mobile_number) -> None:
            self.__gender_mrs_box.check()
            self.__password_field.fill(password)
            self.__days_dropdown.click()
            self.__days_dropdown.select_option("7")
            self.__newsletter_checkbox.check()
            self.__specoffer_checkbox.check()
            self.__first_name.fill(first_name)
            self.__last_name.fill(last_name)
            self.__company_name.fill(company)
            self.__address_one.fill(address_one)
            self.__address_two.fill(address_two)
            self.__state.fill(state)
            self.__city.fill(city)
            self.__zip_code.fill(zip_code)
            self.__mobile_number.fill(mobile_number)
            self.__create_account_btn.click()


