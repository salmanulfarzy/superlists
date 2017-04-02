from .base import FunctionalTest
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        #  Edith goes to the home page and accidentally tries to submit
        #  an emoty list ite. She hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        #  The home page refreshes, and there is a error message saying
        #  that list items cannot be blank
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
            ))

        #  She tries again with some text for the item, Which now works
        self.get_item_input_box().send_keys('Buy Milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Milk')

        #  Perversely, she now decides to submit a second blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        #  She receives a similar warning no the list page
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
            ))

        #  And she can correct it by filling some text in
        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Milk')
        self.wait_for_row_in_list_table('2: Make tea')

