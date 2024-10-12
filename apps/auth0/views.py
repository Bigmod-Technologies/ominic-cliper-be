# utils

from drf_spectacular.utils import extend_schema

# auth
from dj_rest_auth.views import (
    LoginView,
)

# Create your views here.


@extend_schema(tags=["Auth"])
class UserLoginView(LoginView):
    def login(self):
        return super().login()
