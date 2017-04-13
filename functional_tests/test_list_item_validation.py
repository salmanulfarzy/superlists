from .base import FunctionalTest
from .list_page import ListPage
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        #  Edith goes to the home page and accidentally tries to submit
        #  an emoty list ite. She hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        ListPage(self).get_item_input_box().send_keys(Keys.ENTER)

        #  The browser intercepts the request, and does not load the list page
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:invalid'
            ))

        #  She tries again with some text for the new item and the error
        #  disappears
        ListPage(self).get_item_input_box().send_keys('Buy Milk')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:valid'
            ))

        #  And she can submit it successfully
        ListPage(self).get_item_input_box().send_keys(Keys.ENTER)
        ListPage(self).wait_for_row_in_list_table('Buy Milk', 1)

        #  Perversely, she now decides to submit a second blank list item
        ListPage(self).get_item_input_box().send_keys(Keys.ENTER)

        #  Again the browser will not comply
        ListPage(self).wait_for_row_in_list_table('Buy Milk', 1)
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:valid'
            ))

        #  And she can correct it by filling some text in
        ListPage(self).get_item_input_box().send_keys('Make tea')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:valid'
            ))
        ListPage(self).get_item_input_box().send_keys(Keys.ENTER)
        ListPage(self).wait_for_row_in_list_table('Buy Milk', 1)
        ListPage(self).wait_for_row_in_list_table('Make tea', 2)

    def test_cannot_add_duplicate_items(self):
        #  Edith goes to the home page and starts a new list
        self.browser.get(self.live_server_url)
        ListPage(self).add_list_item('Buy Apple')

        #  She accidentally tries to enter a duplicate item
        ListPage(self).get_item_input_box().send_keys('Buy Apple')
        ListPage(self).get_item_input_box().send_keys(Keys.ENTER)

        #  She sees a helpful message
        self.wait_for(lambda: self.assertEqual(
                self.get_error_element().text,
                "You've already got this in your list"
                ))

    def test_error_messages_are_cleared_on_input(self):
        #  Edith start a list and causes a validation error
        self.browser.get(self.live_server_url)
        ListPage(self).add_list_item('Hodor')
        ListPage(self).get_item_input_box().send_keys('Hodor')
        ListPage(self).get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertTrue(
            self.get_error_element().is_displayed()
            ))

        #  She starts typing in the input box box to clear the error
        ListPage(self).get_item_input_box().send_keys('a')

        #  She is pleased to see that the errror message disappears
        self.wait_for(lambda: self.assertFalse(
            self.get_error_element().is_displayed()
            ))
