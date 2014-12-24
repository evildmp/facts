import sys

from django.test import LiveServerTestCase
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium

from facts.models import Fact


class NewVisitorTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super(NewVisitorTest, cls).setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super(NewVisitorTest, cls).tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_sees_an_empty_page_message(self):
        # visit the home page of the facts appplication
        self.browser.get(self.server_url)

        # the default title of the home page is "Facts"
        self.assertIn("Facts", self.browser.title)

        # the default h1 is also "Facts"
        h1_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Facts", h1_text)

    def test_ul_of_facts(self):
        first_fact = Fact.objects.create(text="This is the first fact")
        second_fact = Fact.objects.create(text="This is the second fact")

        self.browser.get(self.server_url)

        li_items = self.browser.find_elements_by_tag_name("li")

        self.assertIn("This is the first fact", li_items[0].text)
        self.assertIn("This is the second fact", li_items[1].text)

class AdminUserTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super(AdminUserTest, cls).setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super(AdminUserTest, cls).tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        # pass
        self.browser.quit()

    # def test_admin_user_can_login(self):
    #     # create a user
    #     user = User.objects.create_user(username='admin', email='admin@example.com', password='admin')
    #
    #     # go to the login page and login as admin
    #     self.browser.get(
    #         '%s%s' % (self.server_url, "/admin/login/")
    #     )
    #
    #     username = self.browser.find_element_by_id("id_username")
    #     username.send_keys("admin")
    #
    #     password = self.browser.find_element_by_id("id_password")
    #     password.send_keys("admin")
    #
    #     self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
    #
    #     # go to the main admin page
    #     self.browser.get(
    #         '%s%s' % (self.server_url, "/admin/")
    #     )
    #     # we're in the admin
    #     self.assertIn("Admin", self.browser.title)
