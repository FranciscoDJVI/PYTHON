from django.urls import URLPattern, path

from . import views

app_name = "paysystem_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id_product>/", views.detail, name="detail")
]
