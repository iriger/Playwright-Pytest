import pytest
import  allure

from pages.check_boxes_page import CheckBox
from utils.tools import take_screenshot


class TestCheckBoxes:

    @pytest.fixture
    def test_setup(self, new_page, base_url):
        self.page = new_page
        # self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.checkbox = CheckBox(self.page)
        self.page.goto(f"{base_url}/checkbox")

        # self.page.goto('https://demoqa.com/checkbox', wait_until='load', timeout=60000)

    def test_text_boxes(self, test_setup):
        """Test to verify the checkboxes on the page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.checkbox.expand_home_directory()

        self.checkbox.select_checkbox('Downloads')
        self.checkbox.check_results('Downloads')

        self.checkbox.select_checkbox('documents')
        self.checkbox.check_results('documents')

        self.checkbox.select_checkbox('desktop')
        self.checkbox.check_results('desktop')
        take_screenshot(self.page, "checkbox desktop")