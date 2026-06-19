from rest_framework import routers

from django.urls import path, include

from musician.views import MusicianViewSet

router = routers.DefaultRouter()

router.register(
    "manage",
    MusicianViewSet
)

urlpatterns = [
    path(
        "",
        include(router.urls),
        name="manage",
    ),
]

app_name = "musician"
