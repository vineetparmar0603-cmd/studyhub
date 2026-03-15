from django.shortcuts import render
from groups.models import Group

# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')

def dashboard(request):
    return render(request,'mainapp/dashboard.html')

def dashboard(request):

    user_groups = Group.objects.filter(members=request.user)

    context = {
        'groups': user_groups
    }

    return render(request, 'mainapp/dashboard.html', context)