import datetime

from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from petstagram.main.validators import validate_only_letters, validate_file_max_size_in_mb


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    # It is the same
    # GENDERS = [
    #     ('Male', 'Male'),
    #     ('Female', 'Female'),
    #     ('DO_NOT_SHOW', 'DO_NOT_SHOW')
    # ]

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

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
    )


class Pet(models.Model):
    # Constants
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = "Parrot"
    FISH = 'Fish'
    OTHER = 'Other'

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
    NAME_MAX_LENGTH = 30

    # Fields(Colums)
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    # Relations
    # - one to one
    # - one to many

    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    # - many to many

    # Properties


@property
def age_of(self):
    return datetime.datetime.now().year - self.date_of_birth.year

    # Methods

    # dunder methods

    # Meta


class Meta:
    unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            # validate_file_max_size_in_mb(5),
        )
    )

    tagged_pets = models.ManyToManyField(
        Pet,

        # validate at least one pet
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )
