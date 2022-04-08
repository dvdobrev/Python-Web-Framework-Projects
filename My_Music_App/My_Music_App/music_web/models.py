from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

USER_NAME_VALIDATION_ERROR_MSG = "Ensure this value contains only letters, numbers, and underscore."
ALLOWED_SYMBOLS = '_'


def user_name_validator(value):
    if not value.isalnum() and not '_' in value:
        raise ValidationError(USER_NAME_VALIDATION_ERROR_MSG)


class Profile(models.Model):
    USER_NAME_MAX_LENGTH = 15
    USER_NAME_MIN_LENGTH = 2

    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USER_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USER_NAME_MIN_LENGTH),
            user_name_validator,
        )
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30

    ARTIST_NAME_MAX_LEN = 30

    GENRE_NAME_MAX_LEN = 30

    MIN_PRICE = 0.0

    MUSIC_GENRE = [
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', "Jazz Music"),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    ]

    album_name = models.CharField(
        max_length=ALBUM_NAME_MAX_LEN,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_NAME_MAX_LEN,
        unique=True,
    )

    genre = models.CharField(
        max_length=GENRE_NAME_MAX_LEN,
        choices=MUSIC_GENRE,

    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()
    # image_url = models.URLField(verbose_name='Image URL:')  # a way to make a label

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE),
        )
    )
