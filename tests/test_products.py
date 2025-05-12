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


class TestProducts:

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


    def test_products(self, test_setup):
        assert self.home_page.is_main_section_visible()
        self.home_page.goto_products_page()
        assert self.products_page.is_product_page_title_visible()
        self.products_page.goto_product_details()
        assert self.product_details_page.is_product_card_visible()
        assert self.product_details_page.is_product_name_visible()
        assert self.product_details_page.is_product_category_visible()
        assert self.product_details_page.is_product_price_visible()
        assert self.product_details_page.is_product_availability_visible()
        assert self.product_details_page.is_product_condition_visible()
        assert self.product_details_page.is_product_brand_visible()

    def test_product_search(self, test_setup):
        assert self.home_page.is_main_section_visible()
        self.home_page.goto_products_page()
        assert self.products_page.is_product_page_title_visible()
        self.products_page.search_product(Data.search_option)
        assert self.products_page.is_search_results_title_visible()
        assert self.products_page.is_products_search_results_contain_search_option(Data.search_option)
