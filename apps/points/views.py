from django.shortcuts import render
from points.models.matchday import MatchDay
from points.models.points import PlayerPoints
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import MatchDayCreateForm,PlayerPointsCreateForm
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
    template_name = 'points/PlayerPoints/create.html'  # Update with your actual template name
    success_url = reverse_lazy('points:playerpoints_list')  # Update with your actual success URL

    def form_valid(self, form):
        # Optionally, you can perform additional actions when the form is valid
        return super().form_valid(form)
