from django.shortcuts import render
from players.models.teams import Teams
from players.models.players import Player
from players.models.userteam import UserSelection
from players.forms import TeamCreateForm, PlayerCreateForm, UserTeamCreateForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from decorators import has_roles
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


@method_decorator(login_required(), name='dispatch')
@method_decorator(has_roles(['admin']), name='dispatch')
class TeamListView(ListView):
    model = Teams
    template_name = 'players/teams/list.html'
    context_object_name = 'team_list'  # Specify the variable name in the template

    def get_queryset(self):
        # Customize the queryset if needed
        return Teams.objects.all()

@method_decorator(login_required(), name='dispatch')
@method_decorator(has_roles(['admin']), name='dispatch')
class TeamCreateView(CreateView):
    model = Teams
    form_class = TeamCreateForm
    # Update with your actual template name
    template_name = 'players/teams/create.html'
    # Update with your actual success URL
    success_url = reverse_lazy('players:team_list')

    def form_valid(self, form):
        # Optionally, you can perform additional actions when the form is valid
        return super().form_valid(form)



@login_required()
@has_roles(['admin'])
def team_delete(request, pk):
    try:
        teams = Teams.objects.get(pk=pk)
        teams.delete()
        messages.success(request, 'Team deleted successfully.')
    except Teams.DoesNotExist:
        messages.error(request, 'Team not found.')
    except Exception as e:
        messages.error(request, 'Error occurred while deleting the team.')

    return redirect('players:team_list')

@method_decorator(login_required(), name='dispatch')
@method_decorator(has_roles(['admin']), name='dispatch')
class TeamUpdateView(UpdateView):
    model = Teams
    form_class = TeamCreateForm  # Use the same form as in your CreateView
    # Update with your actual template name
    template_name = 'players/teams/update.html'
    # Update with your actual success URL
    success_url = reverse_lazy('players:team_list')

    def form_valid(self, form):
        # Optionally, you can perform additional actions when the form is valid
        return super().form_valid(form)



@method_decorator(login_required(), name='dispatch')
@method_decorator(has_roles(['admin']), name='dispatch')
# Players Views
class PlayerListView(ListView):
    model = Player
    template_name = 'players/player/list.html'
    context_object_name = 'player_list'  # Specify the variable name in the template

    def get_queryset(self):
        # Customize the queryset if needed
        return Player.objects.all()


@method_decorator(login_required(), name='dispatch')
@method_decorator(has_roles(['admin']), name='dispatch')
class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerCreateForm
    # Update with your actual template name
    template_name = 'players/player/create.html'
    # Update with your actual success URL
    success_url = reverse_lazy('players:players_list')

    def form_valid(self, form):
        # Optionally, you can perform additional actions when the form is valid
        return super().form_valid(form)



@login_required()
@has_roles(['admin'])
def player_delete(request, pk):
    try:
        player = Player.objects.get(pk=pk)
        player.delete()
        messages.success(request, 'player deleted successfully.')
    except Player.DoesNotExist:
        messages.error(request, 'player not found.')
    except Exception as e:
        messages.error(request, 'Error occurred while deleting the player.')

    return redirect('players:players_list')


@method_decorator(login_required(), name='dispatch')
@method_decorator(has_roles(['admin']), name='dispatch')
class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerCreateForm  # Use the same form as in your CreateView
    # Update with your actual template name
    template_name = 'players/player/update.html'
    # Update with your actual success URL
    success_url = reverse_lazy('players:players_list')

    def form_valid(self, form):
        # Optionally, you can perform additional actions when the form is valid
        return super().form_valid(form)

# UserTeam views



@method_decorator(login_required(), name='dispatch')
@method_decorator(has_roles(['admin']), name='dispatch')
class UserTeamCreateView(CreateView):
    model = UserSelection
    form_class = UserTeamCreateForm
    # Update with your actual template name
    template_name = 'players/userteam/create.html'
    # Update with your actual success URL
    success_url = reverse_lazy('players:userteam_list')

    def form_valid(self, form):
        # Optionally, you can perform additional actions when the form is valid
        return super().form_valid(form)



@method_decorator(login_required(), name='dispatch')
@method_decorator(has_roles(['admin']), name='dispatch')
class UserTeamListView(ListView):
    model = UserSelection
    template_name = 'players/userteam/list.html'
    # Specify the variable name in the template
    context_object_name = 'userteam_list'

    def get_queryset(self):
        # Customize the queryset if needed
        return UserSelection.objects.all()



@method_decorator(login_required(), name='dispatch')
@method_decorator(has_roles(['admin']), name='dispatch')
class UserTeamUpdateView(UpdateView):
    model = UserSelection
    form_class = UserTeamCreateForm  # Use the same form as in your CreateView
    # Update with your actual template name
    template_name = 'players/userteam/update.html'
    # Update with your actual success URL
    success_url = reverse_lazy('players:userteam_list')

    def form_valid(self, form):
        # Optionally, you can perform additional actions when the form is valid
        return super().form_valid(form)



@login_required()
@has_roles(['admin'])
def userteam_delete(request, pk):
    try:
        userteam = UserSelection.objects.get(pk=pk)
        userteam.delete()
        messages.success(request, 'userteam deleted successfully.')
    except UserSelection.DoesNotExist:
        messages.error(request, 'userteam not found.')
    except Exception as e:
        messages.error(request, 'Error occurred while deleting the userteam.')

    return redirect('players:userteam_list')
