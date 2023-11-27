from django.urls import path, include
from . import views
app_name = "accounts"

urlpatterns = [
    path('pages/', include('accounts.pages.urls')),
    path('', views.home,name="home"),
    path('login/', views.login,name="login")
]
