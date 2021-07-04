
import uuid

from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    """
    A class to represent a employee implements for model.Model.

    ...

    Attributes
    ----------
    unique_id : uuid
        unique identifier
    employee : ForeignKey
        User employee from user
    created : DateField
        create date for row
    modified : DateTimeField
        modified date and time for row
    active : BooleanField
        logic deleted for row
    """
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False,
                                 unique=True)
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        """
        Override __str__ method to return str
        """
        return f"{self.employee.username}"
