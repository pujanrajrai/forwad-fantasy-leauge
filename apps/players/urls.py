from django.urls import path, include
from . import views
app_name = "players"

urlpatterns = [
    path('list/', views.TeamListView.as_view(), name="team_list"),
    path('create/', views.TeamCreateView.as_view(), name='team_create'),
    path('team/delete/<int:pk>', views.team_delete, name="team_delete"),
    path('<int:pk>/update/', views.TeamUpdateView.as_view(), name='team_update'),

    path('list/player/', views.PlayerListView.as_view(), name="players_list"),
    path('create/player/', views.PlayerCreateView.as_view(), name='player_create'),
    path('player/delete/<int:pk>', views.player_delete, name="player_delete"),
    path('<int:pk>/update/player/', views.PlayerUpdateView.as_view(), name='player_update'),

    path('list/userteam/', views.UserTeamListView.as_view(), name="userteam_list"),
    path('create/userteam/', views.UserTeamCreateView.as_view(), name='userteam_create'),
    path('userteam/delete/<int:pk>', views.userteam_delete, name="userteam_delete"),
    path('<int:pk>/update/userteam/', views.UserTeamUpdateView.as_view(), name='userteam_update'),
]
