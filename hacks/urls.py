from django.urls import path
from .views import AddHack, Hacks, HackDetail, DeleteHack, EditHack


urlpatterns = [
    path("add/", AddHack.as_view(), name="add_hack"),
    path("", Hacks.as_view(), name="hacks"),
    path("<slug:pk>/", HackDetail.as_view(), name="hack_detail"),
    path("delete/<slug:pk>/", DeleteHack.as_view(), name="delete_hack"),
    path("edit/<slug:pk>/", EditHack.as_view(), name="edit_hack",),
]
