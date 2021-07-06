import datetime

from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from pytz import timezone

from lunch.models import Menu, Orders, MenuOptions

MENU_CREATE_HOUR = getattr(settings, "MENU_CREATE_HOUR", 8)
LIMIT_HOUR = getattr(settings, "LIMIT_HOUR", 11)
EMPLOYEES_TIME_ZONE = getattr(settings, "EMPLOYEES_TIME_ZONE",
                              "America/Santiago")


class MenuForm(forms.ModelForm):
    """
    A class to create Menu form.
    ...

    Attributes
    ----------
    name : CharField
        menu name
    message : CharField
        menu message for employees
    date : DateField
        date to send menu
    """
    name = forms.CharField(required=True)
    message = forms.CharField()
    date = forms.DateField(required=True, widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    def clean(self):
        """
        Override save method to validate date
        Validate datetime to create menu to send it
        :param args:
        :param kwargs:

        """
        msg = "Nora lo siento, ya no puedes guardar menu para hoy!"
        cleaned_data = super().clean()
        date = cleaned_data.get("date", None)
        if not date:
            assert ValueError("date is required")
            return
        menu_date = datetime.datetime.now(timezone(EMPLOYEES_TIME_ZONE))
        if date < menu_date.date():
            self.add_error("date", msg)
        if date == menu_date.date():
            if datetime.datetime.now(
                    timezone(EMPLOYEES_TIME_ZONE)) >= menu_date.replace(
                hour=MENU_CREATE_HOUR):
                self.add_error("date", msg)
        return

    class Meta:
        """
        Meta class form MenuForm
        :fields: name, message, date
        """
        model = Menu
        fields = ["name", "message", "date"]


class OrderForm(forms.ModelForm):
    """
    A class to create Menu form.
    ...

    Attributes
    ----------
    option : ModelChoiceField
        employee select menu option
    customizations : CharField
        customizations for employee menu option
    """

    def clean(self):
        """
        Override clean method to validate employee date
        :param args:
        :param kwargs:
        """
        order_datetime = datetime.datetime.now(timezone(EMPLOYEES_TIME_ZONE))
        limit_order = order_datetime.replace(hour=LIMIT_HOUR, minute=0)
        if order_datetime >= limit_order:
            raise ValidationError(
                "Lo siento te quedaste sin comer hoy :(!")

    class Meta:
        """
        Meta class form OrderForm
        :fields: option, customizations
        """
        model = Orders
        fields = ["option", "customizations"]
