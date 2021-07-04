""""
Script to create super user nora and employees
"""
import string

from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from employees.models import Employee


def create_employees(employees_num):
    """
    create employees users
    :param employees_num:
    """
    for num_emp in range(employees_num):
        username = "employee_{}".format(
            get_random_string(5, string.ascii_letters)
        )
        email = '{}@cornershop.com'.format(username)
        user = User.objects.create_user(username=username, password='123456',
                                        email=email)
        employee = Employee.objects.create(
            employee=user
        )
        print('username: {}, uuid {}, number {}'.format(
            username, employee.unique_id, num_emp))


def create_nora_user(username="nora"):
    """
    create nora user
    :param username:
    """
    email = '{}@cornershop.com'.format(username)
    try:
        User.objects.get(username=username)
        print('{} already exist'.format(username))
    except User.DoesNotExist:
        user = User.objects.create_user(username=username, password='123456',
                                        email=email)
        can_create_menu = Permission.objects.get(name='Can create menu')
        can_edit_menu = Permission.objects.get(name='Can edit menu')
        can_see_orders = Permission.objects.get(name='Can see orders')
        user.user_permissions.add(can_create_menu)
        user.user_permissions.add(can_edit_menu)
        user.user_permissions.add(can_see_orders)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        print('{} was created successfully'.format(username))
