from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
from .models import Group,Message
from .models import Note
from django.contrib.auth.decorators import login_required

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
    return redirect('group_detail', group_id=group.id)

@login_required
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
        'notes': notes,
        

    }

    return render(request, 'groups/group_detail.html', context)

def group_chat(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    #  Only members allowed
    if request.user not in group.members.all():
        return redirect('group_list')

    messages = Message.objects.filter(group=group).order_by('created_at')

    if request.method == 'POST':
        content = request.POST.get('content')
        

        if content:
            Message.objects.create(
                group=group,
                user=request.user,
                content=content
            )
            return redirect('group_chat', group_id=group.id)

    return render(request, 'groups/group_chat.html', {
        'group': group,
        'messages': messages
    })

def group_members(request, group_id):
    group = Group.objects.get(id=group_id)
    members = group.members.all()

    return render(request, 'groups/group_members.html', {
        'group': group,
        'members': members
    })

@login_required
def leave_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    # Remove user from group
    group.members.remove(request.user)

    return redirect('group_list')  # redirect to group list page 