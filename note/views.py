from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import View
from django.http import Http404
from .models import Note, NoteShare
from .forms import PinForm, SearchForm
from .utils import collectinfo, random_chars


# Create your views here.
class NotesView(View):
    def get(self, request):
        form = PinForm()
        search_form = SearchForm()
        context = {}
        if request.user.is_authenticated:
            context = {
                'form': form,
                'search_form': search_form,
                'notes': Note.objects.filter(user=request.user).order_by('-note_timestamp'),
            }
        return render(request, 'note/note.html', context)

    def post(self, request):
        context = {'form': PinForm()}

        # if red button [x] was pressed
        if request.POST.get('delete'):
            # doesnt require handling (I think)
            try:
                Note.objects.get(pk=request.POST.get('delete')).delete()
            except ObjectDoesNotExist:
                pass

        # if user asked for sharing link
        if request.POST.get('share'):
            #creating obj
            sharelink, created = NoteShare.objects.get_or_create(sharing_userid=request.user.pk)
            if created:
                sharelink.shorten_url = random_chars()
                sharelink.save()
            #printing url to user
            context['shorten_url'] = request.build_absolute_uri() + 'sharing/' + sharelink.shorten_url

        #making search form and handling its data
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            # union querysets for search request
            notes = Note.objects.filter(user=request.user, note_text__contains=search_form.cleaned_data['text']) | \
                    Note.objects.filter(user=request.user, note_title__contains=search_form.cleaned_data['text']) | \
                    Note.objects.filter(user=request.user, note_url__contains=search_form.cleaned_data['text'])
        else:
            notes = Note.objects.filter(user=request.user)

        context['search_form'] = search_form
        context['notes'] = notes.order_by('-note_timestamp')

        newpin = PinForm(request.POST)
        if newpin.is_valid():
            try:
                new_note = Note()
                new_note.user = request.user
                new_note.note_url = newpin.cleaned_data["url"]
                new_note.note_title, new_note.note_text = collectinfo(new_note.note_url)
                new_note.save()
            except ConnectionError:
                # need solution
                pass

        return render(request, 'note/note.html', context)


def share_redirect(request, code):
    form = PinForm()
    search_form = SearchForm()
    try:
        sharelink = NoteShare.objects.get(shorten_url=code)
    except NoteShare.DoesNotExist:
        raise Http404

    context = {
        'form': form,
        'search_form': search_form,
        'notes': Note.objects.filter(user=sharelink.sharing_userid).order_by('-note_timestamp')
    }
    return render(request, 'note/note.html', context)
