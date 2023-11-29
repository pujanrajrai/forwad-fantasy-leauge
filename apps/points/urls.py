from django.urls import path, include
from . import views
app_name = "points"

urlpatterns = [
    path('list/', views.MatchDayListView.as_view(), name="matchday_list"),
    path('create/', views.MatchDayCreateView.as_view(), name="matchday_create"),
    path('<int:pk>/update/', views.MatchDayUpdateView.as_view(), name="matchday_update"),
    
]
