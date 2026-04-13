# Create your views here.
from django.shortcuts import render, redirect
from .models import Feedback

def give_feedback(request):
    if request.method == "POST":
        message = request.POST.get("message")
        rating = request.POST.get("rating")

        Feedback.objects.create(
            user=request.user,
            message=message,
            rating=rating
        )

        return redirect('profile')  # after submit

    return render(request, 'feedback/feedback.html')