from django.db import models
import subprocess
import requests


class Instruction(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    command = models.CharField(max_length=50, verbose_name="command")
    def __unicode__(self):
        return self.name

class Plugin(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    instructions = models.ManyToManyField(Instruction, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    ip = models.CharField(max_length=50, verbose_name="ip")
    plugins = models.ManyToManyField(Plugin)
