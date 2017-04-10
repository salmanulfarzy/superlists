from selenium import webdriver
from .base import FunctionalTest


def quit_if_possible(browser):
    try:
        browser.quit()
    except:
        pass


class SharingTest(FunctionalTest):

    def test_can_share_a_list_with_another_user(self):
        #  Edith is a logged in user
        self.create_pre_authenticated_session('edith@example.com')
        edith_browser = self.browser
        self.addCleanup(lambda: quit_if_possible(edith_browser))

        #  Her friend gandalf is also hanging out on the lists site
        gandalf_browser = webdriver.Firefox()
        self.addCleanup(lambda: quit_if_possible(gandalf_browser))
        self.browser = gandalf_browser
        self.create_pre_authenticated_session('gandalf@example.com')

        #  Edith goes to the homepage and starts a list
        self.browser = edith_browser
        self.browser.get(self.live_server_url)
        self.add_list_item('Get ring')

        #  She notices a "share this list" option
        share_box = self.browser.find_element_by_css_selector(
                'input[name="sharee"'
                )
        selg.assertEqual(
                share_box.get_attribute('placeholder'),
                'your-friend@example.com'
                )
