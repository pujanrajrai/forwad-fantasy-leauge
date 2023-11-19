from django.urls import path, include

app_name = "pages"

urlpatterns = [
    path('usermanagement/', include('accounts.pages.usermanagement.urls')),
]
