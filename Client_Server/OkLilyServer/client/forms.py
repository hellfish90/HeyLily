__author__ = 'Marc'
from django.forms import ModelForm
from OkLilyServer.models import *


class JobForm(ModelForm):

    class Meta:
        model = Job
        fields = ('name', 'plugin', 'instruction', 'command', 'state')
