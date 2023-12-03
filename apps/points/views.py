from django.shortcuts import render
from points.models.matchday import MatchDay
from points.models.points import PlayerPoints
from points.models.teamresult import TeamResult
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import MatchDayCreateForm,PlayerPointsCreateForm,TeamResultCreateForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
# Create your views here.
class MatchDayListView(ListView):
    model = MatchDay
    template_name = 'points/matchday/list.html'
    context_object_name = 'matchday_list'  # Specify the variable name in the template

    def get_queryset(self):
        # Customize the queryset if needed
        return MatchDay.objects.all()

class MatchDayCreateView(CreateView):
    model = MatchDay
    form_class = MatchDayCreateForm
    template_name = 'points/matchday/create.html'  # Update with your actual template name
    success_url = reverse_lazy('points:matchday_list')  # Update with your actual success URL

    def form_valid(self, form):
        # Optionally, you can perform additional actions when the form is valid
        return super().form_valid(form)

class MatchDayUpdateView(UpdateView):
    model = MatchDay
    form_class = MatchDayCreateForm  # Use the same form as in your CreateView
    template_name = 'points/matchday/update.html'  # Update with your actual template name
    success_url = reverse_lazy('points:matchday_list')  # Update with your actual success URL

    def form_valid(self, form):
        # Optionally, you can perform additional actions when the form is valid
        return super().form_valid(form)


# Player Points
class PlayerPointsListView(ListView):
    model = PlayerPoints
    template_name = 'points/playerpoint/list.html'
    context_object_name = 'playerpoint_list'  # Specify the variable name in the template

    def get_queryset(self):
        # Customize the queryset if needed
        return PlayerPoints.objects.all()


class PlayerPointsCreateView(CreateView):
    model = PlayerPoints
    form_class = PlayerPointsCreateForm
    template_name = 'points/playerpoint/create.html'  # Update with your actual template name
    success_url = reverse_lazy('points:playerpoint_list')  # Update with your actual success URL

    def form_valid(self, form):
        # Optionally, you can perform additional actions when the form is valid
        return super().form_valid(form)

class PlayerPointUpdateView(UpdateView):
    model = PlayerPoints
    form_class = PlayerPointsCreateForm  # Use the same form as in your CreateView
    template_name = 'points/playerpoint/update.html'  # Update with your actual template name
    success_url = reverse_lazy('points:playerpoint_list')  # Update with your actual success URL

    def form_valid(self, form):
        # Optionally, you can perform additional actions when the form is valid
        return super().form_valid(form)



# Team Result
class TeamResultListView(ListView):
    model = TeamResult
    template_name = 'points/teamresult/list.html'
    context_object_name = 'teamresult_list'  # Specify the variable name in the template

    def get_queryset(self):
        # Customize the queryset if needed
        return TeamResult.objects.all()


class TeamResultCreateView(CreateView):
    model = TeamResult
    form_class = TeamResultCreateForm
    template_name = 'points/teamresult/create.html'  # Update with your actual template name
    success_url = reverse_lazy('points:teamresult_list')  # Update with your actual success URL

    def form_valid(self, form):
        # Optionally, you can perform additional actions when the form is valid
        return super().form_valid(form)

class TeamResultUpdateView(UpdateView):
    model = TeamResult
    form_class = TeamResultCreateForm  # Use the same form as in your CreateView
    template_name = 'points/teamresult/update.html'  # Update with your actual template name
    success_url = reverse_lazy('points:teamresult_list')  # Update with your actual success URL

    def form_valid(self, form):
        # Optionally, you can perform additional actions when the form is valid
        return super().form_valid(form)
