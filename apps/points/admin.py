from django.contrib import admin

# Register your models here.
from points.models.matchday import MatchDay
from points.models.teamresult import TeamResult


admin.site.register([MatchDay, TeamResult])
