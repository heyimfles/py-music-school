from rest_framework import routers

from django.urls import path, include

from musician.views import MusicianViewSet

router = routers.DefaultRouter()

router.register(
    "manager-list",
    MusicianViewSet
)

urlpatterns = [
    path(
        "",
        include(router.urls),
        name="manager-list",
    ),
]

app_name = "musician"
