from django.shortcuts import render, redirect, get_object_or_404
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
    prof = get_object_or_404(Profile,name=name)
    if request.method == "POST":
        prof.email = request.POST.get("email")
        prof.save()
        return redirect("profile-views")
    else:
        return render(request,"profile_email_update.html",{"person":prof})


def profile_renderer(request):
    obj = Profile.objects.all()
    return render(request, "profile.html", {"saved_names": obj})

def specific_profile_show(request,name):
    person = get_object_or_404(Profile,name=name)
    return render(request,"indiviudal_profile.html",{"person":person})

