import pytest
import allure

from faker import Faker

faker = Faker()

from conftest import new_page
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.account_info_page import AccountInfoPage
from pages.account_created_page import AccountCreatedPage
from pages.delete_account_page import DeleteAccountPage
from utils.test_data import Data
from utils.tools import take_screenshot


class TestRegistration:

    @pytest.fixture
    def test_setup(self, new_page, base_url):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.signup_login_page = SignupLoginPage(self.page)
        self.account_info_page = AccountInfoPage(self.page)
        self.account_created_page = AccountCreatedPage(self.page)
        self.delete_account_page = DeleteAccountPage(self.page)

        self.page.goto(f"{base_url}", wait_until='networkidle')

    def test_register_user(self,test_setup):
        assert self.home_page.is_main_section_visible()
        self.home_page.go_to_signup_page()
        assert self.signup_login_page.is_signup_title_visible()
        self.signup_login_page.signup(name=faker.name(),email=faker.email())
        assert self.account_info_page.is_account_info_title_visible()
        self.account_info_page.fill_account_info_form(password=faker.password(), first_name= faker.first_name(), last_name=faker.last_name(), company= faker.company(), address_one=faker.street_address(), address_two= faker.secondary_address(), state= faker.state(), city= faker.city(), zip_code= faker.zipcode(), mobile_number= faker.phone_number())
        assert self.account_created_page.is_account_created_title_visible()
        self.account_created_page.continue_account_created()
        assert self.home_page.is_loggedin_as_visible()
        self.home_page.delete_account()
        assert self.delete_account_page.is_account_deleted_title_visible()
        self.delete_account_page.continue_account_deleted()

    def test_login_valid_credentials(self,test_setup):
        assert self.home_page.is_main_section_visible()
        self.home_page.go_to_signup_page()
        assert self.signup_login_page.is_login_form_visible()
        self.signup_login_page.login(Data.valid_email, Data.valid_password)
        assert self.home_page.is_loggedin_as_visible()

    def test_login_invalid_credentials(self, test_setup):
        assert self.home_page.is_main_section_visible()
        self.home_page.go_to_signup_page()
        assert self.signup_login_page.is_login_form_visible()
        self.signup_login_page.login(Data.invalid_email, Data.invalid_password)
        assert  self.signup_login_page.is_login_error_message_visible()

    def test_logout_user(self, test_setup):
        assert self.home_page.is_main_section_visible()
        self.home_page.go_to_signup_page()
        assert self.signup_login_page.is_login_form_visible()
        self.signup_login_page.login(Data.valid_email, Data.valid_password)
        assert self.home_page.is_loggedin_as_visible()
        self.home_page.logout()
        assert self.signup_login_page.is_login_form_visible()

    def test_register_user_existing_email(self, test_setup):
        assert self.home_page.is_main_section_visible()
        self.home_page.go_to_signup_page()
        assert self.signup_login_page.is_signup_title_visible()
        self.signup_login_page.signup(name=faker.name(), email=Data.valid_email)
        assert self.signup_login_page.is_signup_error_message_visible()







