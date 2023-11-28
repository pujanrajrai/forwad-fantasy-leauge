from django.shortcuts import render
from points.models.matchday import MatchDay
# Create your views here.
class MatchDayListView(ListView):
    model = MatchDay
    template_name = 'points/matchday/list.html'
    context_object_name = 'matchday_list'  # Specify the variable name in the template

    def get_queryset(self):
        # Customize the queryset if needed
        return MatchDay.objects.all()
