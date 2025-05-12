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
from pages.contact_us_page import ContactUsPage
from pages.te_cases_page import TeCasesPage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from utils.test_data import Data
from utils.tools import take_screenshot


class TestNavigationToOtherPages:

    @pytest.fixture
    def test_setup(self, new_page, base_url):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.signup_login_page = SignupLoginPage(self.page)
        self.account_info_page = AccountInfoPage(self.page)
        self.account_created_page = AccountCreatedPage(self.page)
        self.delete_account_page = DeleteAccountPage(self.page)
        self.contact_us_page = ContactUsPage(self.page)
        self.te_cases_page = TeCasesPage(self.page)
        self.products_page = ProductsPage(self.page)
        self.product_details_page = ProductDetailsPage(self.page)

        self.page.goto(f"{base_url}", wait_until='networkidle')

    def test_contact_us(self, test_setup):
        assert self.home_page.is_main_section_visible()
        self.home_page.goto_contact_us()
        assert self.contact_us_page.is_get_get_in_touch_title_visible()
        self.contact_us_page.write_and_submit_message(name=faker.name(), email=faker.email(), subject=faker.sentence(nb_words=5), message=faker.paragraph(nb_sentences=4))
        assert  self.contact_us_page.is_message_submit_success_visible()
        self.home_page.goto_home()
        assert self.home_page.is_main_section_visible()

    def test_test_cases(self, test_setup):
        assert self.home_page.is_main_section_visible()
        self.home_page.goto_test_cases_page()
        assert self.te_cases_page.is_test_cases_page_title_visible()


    def test_subscription(self,test_setup):
        assert self.home_page.is_main_section_visible()
        self.page.pause()
        self.home_page.goto_footer()
        assert self.home_page.is_subscription_title_visible()
        self.home_page.subscribe(subscription_email=faker.email())
        assert self.home_page.is_subscription_success_message_visible()
