from django.urls import path
from . import views
app_name = "users"

urlpatterns = [
    path('create/', views.create, name="create_user"),
    path('list/', views.UserListView.as_view(), name="user_list"),
]
