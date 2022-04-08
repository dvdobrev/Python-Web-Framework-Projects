from django.shortcuts import render, redirect

from My_Music_App.music_web.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateAlbumForm, \
    EditAlbumForm, DeleteAlbumForm
from My_Music_App.music_web.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]

    return None


def show_home(request):
    profile = get_profile()
    albums = Album.objects.all()

    if not profile:
        return redirect('create profile page')

    context = {
        'profile': profile,
        'albums': albums,
    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    profile = get_profile()

    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')

    else:
        form = CreateAlbumForm()

    context = {
        'form': form,
        'profile': profile,

    }
    return render(request, 'add-album.html', context)


def album_details_page(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album,

    }

    return render(request, 'album-details.html', context)


def edit_album_page(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show home')

    else:
        form = EditAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,

    }

    return render(request, 'edit-album.html', context)


def album_delete_page(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show home')

    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,

    }
    return render(request, 'delete-album.html', context)


def profile_create_page(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')

    else:
        form = CreateProfileForm()

    context = {
        'form': form,

    }

    return render(request, 'home-no-profile.html', context)


def profile_details_page(request):
    profile = get_profile()
    albums = Album.objects.all()
    total_albums = len(albums)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show_home')

    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
        'total_albums': total_albums,

    }
    return render(request, 'profile-details.html', context)


def delete_profile_page(request):
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show home')

    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)

"""This is better"""
# def delete_profile_page(request):
#     if request.method == 'POST':
#         profile = Profile.objects.first()
#         profile.delete()
#         Album.objects.all().delete()
#         return redirect('show home')
#     return render(request, 'profile-delete.htm')
