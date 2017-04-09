from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2, 512,
                delta = 10
                )
        # Shre start a new list and sees the input is nicely centered
        self.add_list_item('testing')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2, 512,
                delta = 10
                )

