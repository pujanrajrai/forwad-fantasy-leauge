from django.urls import path, include
from . import views
app_name = "users"

urlpatterns = [
    path('profile_redirect/', views.UserProfileRedirectView.as_view(),
         name='profile_redirect'),
    path('create/', views.UserTeamCreateView.as_view(), name='create'),
    path('list/', views.get_userteam, name='list'),
    path('update/<int:pk>/', views.UserTeamUpdateView.as_view(), name='update'),
    path('', views.home,name='home'),
    path('about/', views.about,name='about')
]
