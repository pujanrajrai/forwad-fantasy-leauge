from django.urls import path
from . import views
app_name = "users"

urlpatterns = [
    path('create/', views.create, name="create_user"),
    path('list/', views.UserListView.as_view(), name="user_list"),
    path('users/block/<int:user_id>/', views.BlockUserView.as_view(), name='user_block_device'),
    path('users/unblock/<int:user_id>/', views.UnblockUserView.as_view(), name='user_unblock_device'),
    path('users/profile_redirect/<int:user_id>/', views.UserProfileRedirectView.as_view(), name='profile_redirect'),
]
