from django.shortcuts import render
from django.views import View
from .models import Commentary
# Create your views here.
class GuestbookView(View):
    def get(self, request):
        return render(request, 'guestbook/guestbook.html', {'comments': Commentary.objects.all})

    def post(self, request):
        new_comment = Commentary()
        new_comment.text = request.POST.get('text')
        new_comment.name = request.POST.get('name')
        new_comment.save()
        return render(request, 'guestbook/guestbook.html', {'comments': Commentary.objects.all})