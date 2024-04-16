from django.urls import path
from aplicaciones.login.views import *


urlpatterns = [
    path("", LoginFormView2.as_view(), name="login"),
    path("logout/", LogoutRedirectView.as_view(), name="logout")
]
