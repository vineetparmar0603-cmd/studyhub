from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from groups.models import Group, Note

def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'account/login.html')

def register_view(request):     

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            return redirect('login')

    return render(request, 'account/register.html')

@login_required
def profile(request):
    user = request.user

    uploaded_notes = Note.objects.filter(uploaded_by=user)
    joined_groups = user.study_groups.all()

    return render(request, 'account/profile.html', {
        'user': user,
        'uploaded_notes': uploaded_notes,
        'joined_groups': joined_groups
    })