from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expences_tracker.web.validators import validate_only_letters, MaxSizeInMbValidator

# VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE = 'Ensure this value contains only letters.'


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30

    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        )

    )

    image = models.ImageField(
        upload_to=UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        ),
    # image_url = models.URLField(verbose_name='Image URL:')  # a way to make a label
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    image = models.URLField()

    price = models.FloatField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('title', 'price',)
