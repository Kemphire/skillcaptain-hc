from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import Profile
import json

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

def profile_detail_view(request,pk):
    """
    Description:
    Provide the detail of the profile in json format

    Parameter:

    GET:
    pk (int): primary key of the profile

    PUT:
    name(str) : new name of the profile with pk provided in the url
    email(str): new email of the profile with pk provided in the url

    DELETE:
    NONE
    """
    try:
        profile_obj = get_object_or_404(Profile,pk=pk)
        if request.method == "GET":
            data = {"id":profile_obj.id,"name":profile_obj.name,"email":profile_obj.email}
            return JsonResponse(data)
        elif request.method == "PUT":
            name = request.PUT.get("name")
            email = request.PUT.get("email")
            if name and email:
                profile_obj.name = name
                profile_obj.email = email
            elif not name and email:
                profile_obj.email = email
            elif not email and name:
                profile_obj.name = name
            else:
                return JsonResponse({"message":"provide atleast one field"})
            data = {"id":profile_obj.id,"name":profile_obj.name,"email":profile_obj.email}
            return JsonResponse(data)
        elif request.method == "DELETE":
            profile_obj.delete()
            return JsonResponse({"message":f"Profile successfully deleted! with {pk=}"})
        else:
            return JsonResponse({"messag":"http method not supported"})
    except profile_obj.DoesNotExist:
        return JsonResponse({"message":"profile with given primary key does not exist"})

@csrf_exempt  
def profile_get_or_create(request):
    """
    Description:
    Creates new profile with the provided info otherwise info not provided than
    Get the list of already existing profiles

    Parameters:
    Post:
    name(str): name of the profile which is to be created
    email(str): The email address of the profile

    Get:
    None
    """
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        if name and email:
            profile = Profile(name=name,email=email)
        else:
            return JsonResponse({"message":"missing fields profile can't be created"})
        profile.save()
        serialized_obj = serializers.serialize('json',[profile,])
        data = json.loads(serialized_obj)
        return JsonResponse({"message":"Profile create sucessfully","data":data[0]})
    elif request.method == "GET":
        profiles = Profile.objects.all()
        data = [{"name":profile.name,"email":profile.email} for profile in profiles]
        return JsonResponse(data,safe=False)
    else:
        return JsonResponse({"message":"Method not supported"},status=405)

    
