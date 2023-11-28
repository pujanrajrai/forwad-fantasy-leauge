from django.db import models
from base.models import BaseModel


class MatchDay(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
