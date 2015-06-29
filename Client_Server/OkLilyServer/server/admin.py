from django.contrib import admin
from server.models import *
from OkLilyServer import *

# Register your models here.

admin.site.register(Instruction)
admin.site.register(Plugin)
admin.site.register(Module)