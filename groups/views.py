from django.shortcuts import render , redirect

# Create your views here.
from .models import Group

def create_group(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        description = request.POST.get('description')

        group = Group.objects.create(
            name=name,
            subject=subject,
            description=description,
            creator=request.user
        )

        group.members.add(request.user)

        return redirect('group_list')

    return render(request, 'groups/create_group.html')

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups/group_list.html', {'groups': groups})