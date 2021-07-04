import datetime
import uuid

from django.contrib.auth.models import User
from django.test import TestCase

from employees.models import Employee
from lunch.models import Menu, MenuOptions, Orders


class MenuTestCase(TestCase):
    """
    Test case for menu implements TestCase class
    """

    def setUp(self):
        """
        Setup Menu test case
        """
        user = User.objects.create_user(username="test", password="123456",
                                        email="test@test.com")
        Menu.objects.create(menu_user=user, name="menu1", message="hi1",
                            date=datetime.date.today())
        Menu.objects.create(menu_user=user, name="menu2", message="hi2",
                            date=datetime.date.today())

    def test_menu(self):
        """Test menu name get"""
        menu1 = Menu.objects.get(message="hi1")
        menu2 = Menu.objects.get(message="hi2")
        self.assertEqual(menu1.name, "menu1")
        self.assertEqual(menu2.name, "menu2")

    def test_uuid(self):
        """Test menu unique id uuid field"""
        menu1 = Menu.objects.get(name="menu1")
        self.assertTrue(isinstance(menu1.unique_id, uuid.UUID))

    def test_name_max_length(self):
        """Test menu name max_length"""
        menu1 = Menu.objects.get(name="menu1")
        max_length = menu1._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)

    def test_message_max_length(self):
        """Test menu message max_length"""
        menu1 = Menu.objects.get(name="menu1")
        max_length = menu1._meta.get_field("message").max_length
        self.assertEqual(max_length, 100)

    def test_validate_date(self):
        """Test menu date"""
        menu1 = Menu.objects.get(name="menu1")
        self.assertEqual(menu1.date, datetime.date.today())

    def test_sent(self):
        """Test menu sent"""
        menu1 = Menu.objects.get(name="menu1")
        self.assertEqual(menu1.sent, False)
        menu1.sent = True
        menu1.save()
        self.assertEqual(menu1.sent, True)


class MenuOptionsTestCase(TestCase):
    """
    Test case for menu options implements TestCase class
    """

    def setUp(self):
        """
        Setup Menu options test case
        """
        user = User.objects.create_user(username="test", password="123456",
                                        email="test@test.com")
        menu = Menu.objects.create(menu_user=user, name="menu1", message="hi1",
                                   date=datetime.date.today())
        MenuOptions.objects.create(menu=menu, option='option2')

    def test_menu(self):
        """Correct menu option get"""
        menu_option = MenuOptions.objects.get(option="option2")
        self.assertEqual(menu_option.option, 'option2')

    def test_name_max_length(self):
        """menu option max_length test """
        menu_option = MenuOptions.objects.get(option="option2")
        max_length = menu_option._meta.get_field('option').max_length
        self.assertEqual(max_length, 300)


class OrdersTestCase(TestCase):
    """
    Test case for menu options implements TestCase class
    """

    def setUp(self):
        """
        Setup orders test case
        """
        user = User.objects.create_user(username="test", password='123456',
                                        email="test@test.com")
        employee = Employee.objects.create(employee=user)
        menu = Menu.objects.create(menu_user=user, name='menu1', message='hi1',
                                   date=datetime.date.today())
        self.option = MenuOptions.objects.create(menu=menu, option='option2')
        Orders.objects.create(employee=employee, option=self.option,
                              customizations='sin tomates')

    def test_orders(self):
        """Correct orders get"""
        orders = Orders.objects.get(option=self.option)
        self.assertEqual(orders.customizations, 'sin tomates')
