from django.forms import ModelForm
from server.models import *
from django import forms


class ModuleForm(ModelForm):
    plugins = forms.ModelMultipleChoiceField(
        queryset=Plugin.objects.all()
    )

    class Meta:
        model = Module
        fields = ('name', 'ip', 'plugins')


class PluginForm(ModelForm):
    instructions = forms.ModelMultipleChoiceField(
        queryset=Instruction.objects.all()
    )

    class Meta:
        model = Plugin
        fields = ('name', 'instructions')


class InstructionsForm(ModelForm):
    class Meta:
        model = Instruction
        fields = ('name', 'command')
