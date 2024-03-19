
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have Been Logged In!")
            return redirect('home')
        else:
            messages.error(request, "There was an Error Logging in, Please Try again")
            # Redirect back to the same page with error message
            return redirect('home')  # Assuming 'home' is the name of the URL pattern for this view
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been Logged Out...')
    return redirect('home')  # Assuming 'home' is the name of the URL pattern for this view


def register_user(request):
	return render(request, 'register.html', {})