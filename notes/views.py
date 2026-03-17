from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import PublicNote, Download
from django.contrib.auth.decorators import login_required

def public_notes(request):
    query = request.GET.get('q')

    if query:
        notes = PublicNote.objects.filter(title__icontains=query) | PublicNote.objects.filter(subject__icontains=query)
    else:
        notes = PublicNote.objects.all()

    return render(request, 'notes/public_notes.html', {'notes': notes})


def upload_public_note(request):

    if request.method == 'POST':

        title = request.POST['title']
        subject = request.POST['subject']
        file = request.FILES['file']

        PublicNote.objects.create(
            title=title,
            subject=subject,
            file=file,
            uploaded_by=request.user
        )

        

        return redirect('public_notes')

    return render(request, 'notes/upload_public_note.html')

def download_note(request, note_id):
    note = get_object_or_404(PublicNote, id=note_id)

    # Save download record
    Download.objects.create(user=request.user, note=note)

    # Redirect to file
    return redirect(note.file.url)

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(PublicNote, id=note_id)

    
    if note.uploaded_by == request.user:
        note.delete()

    return redirect('dashboard')  # or 'public_notes'