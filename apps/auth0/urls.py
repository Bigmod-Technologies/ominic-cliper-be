from django.urls import path
from .views import UserLoginView, UserTokenVerifyView, UserRefreshTokenView


# auth
urlpatterns = [
    # URLs that do not require a session or valid token
    path("login/", UserLoginView.as_view(), name="login"),
    path("token/verify/", UserTokenVerifyView.as_view(), name="token_verify"),
    path("token/refresh/", UserRefreshTokenView.as_view(), name="token_refresh"),
]
