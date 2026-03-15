from django.shortcuts import render , redirect

# Create your views here.
from .models import PublicNote

def public_notes(request):

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