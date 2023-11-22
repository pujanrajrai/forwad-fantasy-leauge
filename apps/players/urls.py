from django.urls import path, include
from . import views
app_name = "players"

urlpatterns = [
    path('list/', views.TeamListView.as_view(), name="team_list"),
    path('create/', views.TeamCreateView.as_view(), name='team_create'),
    path('team/delete/<int:pk>', views.team_delete, name="team_delete"),
    path('<int:pk>/update/', views.TeamUpdateView.as_view(), name='team_update'),

    path('list/player/', views.PlayerListView.as_view(), name="players_list"),
]
