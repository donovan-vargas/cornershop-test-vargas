import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from pytz import timezone

from lunch.forms import MenuForm, OrderForm
from lunch.models import Menu, MenuOptions

EMPLOYEES_TIME_ZONE = getattr(settings, "EMPLOYEES_TIME_ZONE",
                              "America/Santiago")
LIMIT_HOUR = getattr(settings, "LIMIT_HOUR", 11)


class MenuFormTestCase(TestCase):
    """
    Menu form test cases
    """

    def setUp(self):
        """
        setup
        """
        self.date = datetime.date.today()

    def test_menu_form(self):
        """
         Menu form test
        """
        date_tomorrow = self.date.replace(day=self.date.day + 1)
        form_data = {'name': 'menu1', 'message': 'que tal',
                     'date': date_tomorrow.strftime('%Y-%m-%d')}
        form = MenuForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_menu_form_required_name(self):
        """
         Menu form test
         required name
        """
        date_tomorrow = self.date.replace(day=self.date.day + 1)
        form_data = {'name': '', 'message': 'que tal',
                     'date': date_tomorrow.strftime('%Y-%m-%d')}
        form = MenuForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_menu_form_required_date(self):
        """
         Menu form test
         required name
        """
        form_data = {'name': 'menu1', 'message': 'que tal'}
        form = MenuForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_date_form(self):
        """
        Validate cant create menu for yesterday
        """
        date_yesterday = self.date.replace(day=self.date.day - 1)
        form_data = {'name': 'menu1', 'message': 'que tal',
                     'date': date_yesterday.strftime('%Y-%m-%d')}
        form = MenuForm(data=form_data)
        self.assertFalse(form.is_valid())


class OrderFormTestCase(TestCase):
    """
    Order form test cases
    """

    def setUp(self):
        """
        setup
        """
        self.date = datetime.date.today()
        user = User.objects.create_user(username="test", password='123456',
                                        email="test@test.com")
        menu = Menu.objects.create(menu_user=user, name='menu1', message='hi1',
                                   date=datetime.date.today())
        self.menu_option = MenuOptions.objects.create(menu=menu,
                                                      option='option2')

    def test_menu_form(self):
        """
         Order form test time
        """
        form_data = {'option': self.menu_option.pk,
                     'customizations': 'sin tomates', }
        form = OrderForm(data=form_data)
        order_datetime = datetime.datetime.now(timezone(EMPLOYEES_TIME_ZONE))
        limit_order = order_datetime.replace(hour=LIMIT_HOUR, minute=0)
        if order_datetime >= limit_order:
            self.assertFalse(form.is_valid())
            return
        self.assertTrue(form.is_valid())
