from django.shortcuts import render
from groups.models import Group
from notes.models import Download

# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')

def dashboard(request):
    return render(request,'mainapp/dashboard.html')

def dashboard(request):

    user_groups = Group.objects.filter(members=request.user)
    downloads = Download.objects.filter(user=request.user)
    downloaded_notes = [d.note for d in downloads]

    context = {
        'groups': user_groups,
        'downloaded_notes': downloaded_notes
    }

    return render(request, 'mainapp/dashboard.html', context)