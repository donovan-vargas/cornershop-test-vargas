import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from lunch.models import Menu
from lunch.tasks import send_menu_employees
from lunch.utils import slack


class SendMenuTaskTestCase(TestCase):
    """
    Celery sent menu to employees test case implement TestCase
    """

    def setUp(self):
        """
        Setup
        """
        self.user = User.objects.create_user(username="test",
                                             password="123456",
                                             email="test@test.com")

    def test_fail(self):
        """asert false if not menu fot today"""
        task = send_menu_employees()
        self.assertFalse(task)

    def test_success(self):
        """asert false if menu fot today"""
        Menu.objects.create(menu_user=self.user, name="menu1", message="hi1",
                            date=datetime.date.today())
        task = send_menu_employees()
        self.assertTrue(task)


class SendMessageSlack(TestCase):
    """
    Test case send message to slack chanel
    """

    def test_send_success(self):
        """Success test"""
        self.assertTrue(slack.send_message_slack("unittest"))

    def test_send_fail(self):
        """False test"""
        self.assertFalse(slack.send_message_slack("unittest", "nochanel"))
