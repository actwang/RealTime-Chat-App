from django.shortcuts import render
from .forms import *
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.conf import settings


# Frontpage
def frontpage_view(request):
    return render(request, 'core/frontpage.html')

# Signup Form
def signup_view(request):
    if request.method == 'POST':
        # When user submits form, create a form instance with the submitted data
        form = SignUpForm(request.POST)
        if form.is_valid():
            # save the user
            user = form.save()
            # log the user in
            login(request, user)
            # redirect to home
            return redirect('frontpage')
    # when user first visits the page(GET), show them a blank form
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})
