from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/",views.profile_detail_view,name="put-delete-get"),
    path("",views.profile_get_or_create,name="profile-get-or-create"),
]