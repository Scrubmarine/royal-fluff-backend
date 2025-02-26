from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=32,
        unique=True,
        error_messages={
            'unique': "This username is already taken.",
            'max_length': "Username must be 32 characters or less."
        },
        validators=[
            MinLengthValidator(5, "Username must be at least 5 characters long."),
            validators.RegexValidator(
                regex=r'^[a-zA-Z0-9._-]+$',
                message="Username must contain only A-Z, a-z, 0-9, and special characters (_, -, .).",
                code='invalid'
            )
        ]
    )
    email = models.EmailField(
        max_length=320,
        unique=True,
        error_messages={
            'unique': "This email is already taken.",
        },
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        error_messages={
            'max_length': "First name must not exceed 150 characters.",
        },
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        error_messages={
            'max_length': "Last name must not exceed 150 characters.",
        },
    )

    def clean(self):
        super().clean()
        try:
            self.username = self._meta.get_field('username').clean(self.username, self)
        except ValidationError as e:
            raise ValidationError({'username': e.messages})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)