from .base import FunctionalTest
from selenium.common.exceptions import WebDriverException
from unittest import skip


class ItemValidationTest(FunctionalTest):

    @skip
    def test_cannot_add_empty_list_items(self):
        #  Edith goes to the home page and accidentally tries to submit
        #  an emoty list ite. She hits Enter on the empty input box

        #  The home page refreshes, and there is a error message saying
        #  that list items cannot be blank

        #  She tries again with some text for the item, Which now works

        #  Perversely, she now decides to submit a second blank list item

        #  She receives a similar warning no the list page

        #  And she can correct it by filling some text in
        self.fail('write me!')

