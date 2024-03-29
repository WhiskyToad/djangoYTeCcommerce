from django.urls import path

from .views import views

app_name = "account"

urlpatterns = [
    path("csrf/", views.get_csrf, name="api-csrf"),
    path("login/", views.login, name="api-login"),
    path("whoami/", views.WhoAmIView.as_view(), name="whoami"),
]
