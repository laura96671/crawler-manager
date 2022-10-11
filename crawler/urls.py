from django.urls import path
from . import views

urlpatterns = [
    path("", views.table_data_db, name="homepage"),
    path("<str:pk>", views.DataDelete.as_view(), name="data_delete")
]