# utils

from drf_spectacular.utils import extend_schema

# auth
from dj_rest_auth.views import (
    LoginView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from dj_rest_auth.jwt_auth import get_refresh_view

# Create your views here.


@extend_schema(tags=["Auth"])
class UserLoginView(LoginView):
    def login(self):
        return super().login()


@extend_schema(tags=["Auth"])
class UserTokenVerifyView(TokenVerifyView):
    pass


refresh_view_class = get_refresh_view()


@extend_schema(tags=["Auth"])
class UserRefreshTokenView(refresh_view_class):
    pass
