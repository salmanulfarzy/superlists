import os
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
from django.contrib.sessions.backends.db import SessionStore
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

User = get_user_model()
MAX_WAIT = 10


def wait(fn):
        def modified_fn(*args, **kwargs):
            start_time = time.time()
            while True:
                try:
                    return fn(*args, **kwargs)
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)
        return modified_fn


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            setattr(self, 'live_server_url', 'http://' + staging_server)

    def tearDown(self):
        self.browser.quit()

    @wait
    def wait_for(self, fn):
        return fn()

    def create_pre_authenticated_session(self, email):
        user = User.objects.create(email=email)
        session = SessionStore()
        session[SESSION_KEY] = user.pk
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session.save()

        #  Visit the domain to set a cookie. 404 pages load faster
        self.browser.get(self.live_server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session.session_key,
            path='/',
            ))

    @wait
    def wait_to_be_logged_in(self, email):
        self.browser.find_element_by_link_text('Logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(email, navbar.text)

    @wait
    def wait_to_be_logged_out(self, email):
        self.browser.find_element_by_name('email')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn(email, navbar.text)

