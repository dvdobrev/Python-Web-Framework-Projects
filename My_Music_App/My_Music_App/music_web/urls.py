from django.urls import path

from My_Music_App.music_web.views import show_home, add_album, edit_album_page, album_delete_page, delete_profile_page, \
    album_details_page, profile_details_page, profile_create_page

urlpatterns = (
    path('', show_home, name='show home'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', album_details_page, name='album details page'),
    path('album/edit/<int:pk>/', edit_album_page, name='edit album page'),
    path('album/delete/<int:pk>/', album_delete_page, name='delete album page'),

    path('profile/create/', profile_create_page, name='create profile page'),
    path('profile/details/', profile_details_page, name='profile details page'),
    path('profile/delete/', delete_profile_page, name='delete profile page'),
)
