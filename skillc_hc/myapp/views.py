from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Profile


def hello(request):
    return HttpResponse("<h1>Hello to everyone.</h1>")


def profile_update(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        mobile_no = request.POST.get("mobile_no", "")
        address = request.POST.get("address", "")
        email = request.POST.get("email", "")
        if name and mobile_no and address:
            try:
                Profile.objects.create(
                    name=name, mobile_no=mobile_no, address=address, email=email
                )
                return redirect("profile")
            except Exception as e:
                return HttpResponse(f"<h1>Failed to save profile: {e}</h1>")
        else:
            return HttpResponse("<h1>Enter valid details!</h1>")
    else:
        names = Profile.objects.all()
        context = {"saved_names": names}
        return render(request, "profile.html", context)


def profile_change(request, name: str):
    if request.method == "POST":
        obj = Profile.objects.filter(name=name)
        obj.email = request.POST.get("email", "")
        obj.address = request.POST.get("address", "")
        obj_all = Profile.objects.all()
        return render(request, "profile.html", {"saved_names": obj_all})
    else:
        return render(request, "profile_email_update.html", {"name_v": name})


def profile_renderer(request):
    obj = Profile.objects.all()
    return render(request, "profile.html", {"saved_names": obj})
