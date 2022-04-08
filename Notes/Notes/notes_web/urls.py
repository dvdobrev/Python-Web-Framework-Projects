from django.urls import path

from Notes.notes_web.views import home_page, add_note_page, edit_note_page, delete_note_page, note_details_page, \
    profile_page, create_profile, delete_profile

urlpatterns = (
    path("", home_page, name='show home'),
    path("add", add_note_page, name='add note page'),
    path("edit/<int:pk>", edit_note_page, name='edit note page'),
    path("delete/<int:pk>", delete_note_page, name='delete note page'),
    path("details/<int:pk>", note_details_page, name='note details page'),

    path("profile", profile_page, name='profile page'),
    path('profile/create', create_profile, name='create profile'),
    path('profile/delete', delete_profile, name='delete profile'),


)
