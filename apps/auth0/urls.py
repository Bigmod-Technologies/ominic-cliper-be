from django.urls import path
from .views import (
    UserLoginView,
)


# auth
urlpatterns = [
    # URLs that do not require a session or valid token
    path("login/", UserLoginView.as_view(), name="login"),
]
