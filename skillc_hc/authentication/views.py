from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, LogInForm


def login_view(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(request, username=username, password=password)
            if user is not "":
                messages.success(request, "You are sucessfully logged in")
                login(request, user)
                return redirect("home")
            else:
                messages.warning(request, "Seems like you entered something wrong!")
                return redirect("login-view")
        else:
            messages.warning(request, "Enter valid details")
            return redirect("login")
    else:
        form = LogInForm()

    return render(request, "log_in_template.html", {"form": form})


def register_view(request) -> HttpResponse:
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are sucessfully registered")
            return redirect("login")
        else:
            messages.warning(request, "Enter valid details")
            return redirect("login")
    else:
        form = SignUpForm()

    return render(request, "registeration.html", {"form": form})


@login_required(login_url="login")
def logout_view(request) -> HttpResponse:
    logout(request)
    messages.success(request, "You are sucessfully logged out")
    return redirect("login")
