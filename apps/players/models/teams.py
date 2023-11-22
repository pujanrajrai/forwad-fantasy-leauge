from base.models import BaseModel
from django.db import models


class Teams(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name
