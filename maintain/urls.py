from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("defaultcar/<int:car_id>", views.set_default_car, name="defaultcar"),
    path("mileage", views.car_mileage_view, name="car_mileage"),
    path("service", views.car_service_view, name="car_service"),
    path("plotlogs", views.mileage_logs, name="plotlogs"),
    path("servicedata", views.service_data),
    path("csvdata", views.csv_data, name="csvdata"),
]