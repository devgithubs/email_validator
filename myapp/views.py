from django.shortcuts import render, redirect
from django.http import Http404
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Word
from .forms import TextForm


@require_http_methods(["GET"])
def text_list(request):
    """
    Handles the GET requests for the email list.
    On GET, renders the email list from the database.
    """
    emails = Word.objects.all()
    return render(request, 'text_list.html', {'emails': emails})


def validate_email(email):
    """
    Helper function for text_form:
    Validate email based on the following conditions:
    1. The email cannot be longer than 255 characters
    2. Yahoo, Gmail, and Hotmail email addresses are not accepted.
    3. The email must not already exist in the database.
    """
    if email.endswith(('yahoo.com', 'gmail.com', 'hotmail.com')):
        return False, "Email cannot end with 'yahoo.com', 'gmail.com', 'hotmail.com'."
    elif len(email) > 255:
        return False, 'Email cannot be longer than 255 characters'
    elif Word.objects.filter(text=email).exists():
        return False, "Email already exists."
    return True, ""


@require_http_methods(["GET", "POST"])
def text_form(request):
    """
    Handles the GET and POST requests for the email form.
    On GET, renders the email form template.
    On POST, validates the email and saves it to the database if it is valid.
    """
    if request.method == "GET":
        form = TextForm()
        return render(request, 'text_form.html', {'form': form})
    else:
        form = TextForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('text')
            valid, message = validate_email(email)
            if valid:
                form.save()
                messages.success(request, 'Email is saved.')
                return redirect('text_list')
            else:
                messages.warning(request, message)
                return render(request, 'text_form.html', {'form': form})
        else:
            messages.warning(request, 'Invalid Email')
            return render(request, 'text_form.html', {'form': form})