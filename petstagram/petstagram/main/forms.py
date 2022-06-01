from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from petstagram.main.models import Profile, PetPhoto, Pet
from petstagram.main.validators import MaxDateValidator
from petstagram.main.views.helpers import BootstrapFormMixin, DisabledFieldsFormMixin


class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),

            'picture': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Enter URL',
                }
            ),

        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),

            'picture': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Enter URL',
                }
            ),

            # 'gender': forms.ChoiceField(
            #     choices=Profile.GENDERS,
            #     initial=Profile.DO_NOT_SHOW,
            # ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3
                }
            ),

            'date_of_birth': forms.DateInput(
                attrs={
                    'min': '1920-01-01',
                }
            ),

        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        # exclude = ('first_name', 'last_name', 'email', 'picture', 'date_of_birth', 'description', 'gender')
        fields = ()


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name'
                }
            ),
        }


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def clean_date_of_birth(self):
        MaxDateValidator(date.today())(self.cleaned_data['date_of_birth'])
        return self.cleaned_data['date_of_birth']


    class Meta:
        model = Pet
        exclude = ('user_profile',)


class DeletePetForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    # disabled_fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        exclude = ('user_profile',)
