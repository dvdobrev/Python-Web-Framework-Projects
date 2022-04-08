from django.shortcuts import render, redirect

from Notes.notes_web.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from Notes.notes_web.models import Profile, Note


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]

    return None


def home_page(request):
    profile = get_profile()
    notes = Note.objects.all()

    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
        'notes': notes,

    }
    return render(request, 'home-with-profile.html', context)


def add_note_page(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')

    else:
        form = CreateNoteForm()

    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note_page(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show home')

    else:
        form = EditNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-edit.html', context)


def delete_note_page(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show home')

    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-delete.html', context)


def note_details_page(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)


def create_profile(request):
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


def profile_page(request):
    profile = get_profile()
    notes = Note.objects.all()
    total_notes = len(notes)

    context = {
        'profile': profile,
        'notes': notes,
        'total_notes': total_notes,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    get_profile().delete()
    Note.objects.all().delete()

    return redirect('show home')
