
import uuid

from django.contrib.auth.models import User
from django.db import models

from employees.models import Employee


class Menu(models.Model):
    """
    A class to represent a Menu implements for model.Model.
    ...

    Attributes
    ----------
    menu_user : ForeignKey
        User who created menu item
    name : CharField
        Menu name
    message : CharField
        message for employees
    date : DateField
        date when the menu is sent to employees
    sent : BooleanField
        if the menu was sent True
    created : DateField
        create date for row
    modified : DateTimeField
        modified date and time for row
    active : BooleanField
        logic deleted for row
    """
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False,
                                 unique=True)
    menu_user = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="menu")
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    date = models.DateField(null=False, blank=False)
    sent = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ("can_create_menu", "Can create menu"),
            ("can_edit_menu", "Can edit menu"),
        )

    def __str__(self):
        """
        Override __str__ method to return str
        """
        return f"{self.name}"


class MenuOptions(models.Model):
    """
    A class to represent a MenuOptions implements for model.Model.
    ...

    Attributes
    ----------
    menu : ForeignKey
        Menu item
    option : CharField
        Options for menu
    created : DateField
        create date for row
    modified : DateTimeField
        modified date and time for row
    active : BooleanField
        logic deleted for row
    """
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, null=False, blank=False, related_name="menu_option")
    option = models.CharField(max_length=300, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        """
        Override __str__ method to return str
        """
        return f"{self.option}"


class Orders(models.Model):
    """
    A class to represent a MenuOptions implements for model.Model.
    ...

    Attributes
    ----------
    employee : ForeignKey
        Employee user
    option : ForeignKey
        Options for MenuOptions
    customizations : TextField
        customizations for employee
    created : DateField
        create date for row
    modified : DateTimeField
        modified date and time for row
    active : BooleanField
        logic deleted for row
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                 related_name="order_employee")
    option = models.ForeignKey(MenuOptions, on_delete=models.CASCADE,
                               related_name="order_option")
    customizations = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ("can_see_orders", "Can see orders"),
        )

    def __str__(self):
        """Return Order User and date """
        return "{username} solicito el menu: {menu} opcion: {option}, para {date}".format(
            username=self.employee,
            option=self.option.option,
            menu=self.option.menu,
            date=self.option.menu.date
        )
