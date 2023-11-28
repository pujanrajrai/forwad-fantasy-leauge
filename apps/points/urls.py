from django.urls import path, include
from . import views
app_name = "points"

urlpatterns = [
    path('list/', views.MatchDayListView.as_view(), name="matchday_list"),
    
]
