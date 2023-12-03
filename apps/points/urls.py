from django.urls import path, include
from . import views
app_name = "points"

urlpatterns = [
    path('list/', views.MatchDayListView.as_view(), name="matchday_list"),
    path('create/', views.MatchDayCreateView.as_view(), name="matchday_create"),
    path('<int:pk>/update/', views.MatchDayUpdateView.as_view(), name="matchday_update"),
    
    path('playerpoint/list/', views.PlayerPointsListView.as_view(), name="playerpoint_list"),
    path('playerpoint/create/', views.PlayerPointsCreateView.as_view(), name="playerpoint_create"),
    path('playerpoint/<int:pk>/update/', views.PlayerPointUpdateView.as_view(), name="playerpoint_update"),
    
    path('teamresult/list/', views.TeamResultListView.as_view(), name="teamresult_list"),
    path('teamresult/create/', views.TeamResultCreateView.as_view(), name="teamresult_create"),
    path('teamresult/<int:pk>/update/', views.TeamResultUpdateView.as_view(), name="teamresult_update"),

]
