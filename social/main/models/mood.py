from django.db import models
from django.contrib.auth.models import User


class Mood(models.Model):
    """
    A simple mood model that contains a user description
    of the mood and an associated color.
    """

    # a description of the mood by the user
    description = models.CharField(max_length=128)

    # datetime field auto created on new instance
    created_at = models.DateTimeField(auto_now_add=True)

    # store a hex rgb color for the mood
    color = models.CharField(max_length=6)

    # the user that saved their mood
    user = models.ForeignKey(User)
