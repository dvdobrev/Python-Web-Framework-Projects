import os

from django import forms

from My_Music_App.music_web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age',)
        widget = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),

            'age': forms.TextInput(
                attrs={
                    'age': 'Age',
                }
            ),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age',)


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price',)
        widget = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),

            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),

            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')


class DeleteAlbumForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        # albums_image_path = Album.image_url.
        # Album.objects.all().delete()
        # os.remove(albums_image_path)
        return self.instance

    class Meta:
        model = Album
        fields = ()


"""YOU CAN USE ALSO THIS WAY"""
# class DeleteAlbumForm(CreateAlbumForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for (_, field) in self.fields.items():
#             field.widget.attrs['disabled'] = 'disabled'
#             field.widget.attrs['readonly'] = 'readonly'
#
