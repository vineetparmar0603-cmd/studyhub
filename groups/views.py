from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
from .models import Group
from .models import Note

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

def join_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    group.members.add(request.user)
    return redirect('dashboard')

def group_list(request):

    query = request.GET.get('q')

    if query:
        groups = Group.objects.filter(name__icontains=query)
    else:
        groups = Group.objects.all()

    context = {
        'groups': groups
    }

    return render(request, 'groups/group_list.html', context)

def upload_note(request, group_id):

    group = Group.objects.get(id=group_id)

    if request.method == 'POST':
        title = request.POST['title']
        file = request.FILES['file']

        Note.objects.create(
            group=group,
            title=title,
            file=file,
            uploaded_by=request.user
        )

        return redirect('group_detail', group_id=group.id)

    return render(request, 'groups/upload_note.html', {'group': group})

def group_detail(request, group_id):

    group = Group.objects.get(id=group_id)
    notes = Note.objects.filter(group=group)

    context = {
        'group': group,
        'notes': notes
    }

    return render(request, 'groups/group_detail.html', context)