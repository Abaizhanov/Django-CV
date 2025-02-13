from django.shortcuts import render, redirect
from .forms import CVForm
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.conf import settings
from .models import CV


def create_cv(request):
    if request.method == "POST":
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cv_list')
    else:
        form = CVForm()

    return render(request, 'cv_form.html', {'form': form})

def share_cv_email(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)
    recipient_email = request.POST.get('email')

    if recipient_email:
        subject = f"{cv.name}'s CV"
        message = f"Check out {cv.name}'s CV at {request.build_absolute_uri(cv.profile_picture.url)}"
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])
        messages.success(request, "CV shared successfully via email.")
    else:
        messages.error(request, "Please provide a valid email.")

    return redirect('cv_list')


def contact_view(request):
    return None