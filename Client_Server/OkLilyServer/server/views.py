from rest_framework.exceptions import PermissionDenied
from server.forms import *
from server.models import *
from OkLilyServer.models import *
from django.views.generic import CreateView, ListView, UpdateView
from django.http import HttpResponse

# Create your views here.

""" MODULE  """


class ModuleCreate(CreateView):
    model = Module
    template_name = 'Module/form_create_module.html'
    form_class = ModuleForm
    success_url = "/server/module/"

    def form_valid(self, form):
        if self.request.method == 'POST':
            return super(ModuleCreate, self).form_valid(form)
        return PermissionDenied


class ModuleModify(UpdateView):
    model = Module
    template_name = 'Module/form_create_module.html'
    form_class = ModuleForm
    success_url = "/server/module/"

    def form_valid(self, form):
        if self.request.method == 'POST':
            return super(ModuleModify, self).form_valid(form)
        raise PermissionDenied


class ListModule(ListView):
    model = Module
    template_name = 'Module/list_module.html'

    def get_context_data(self, **kwargs):
        kwargs['module_list'] = Module.objects.all()
        kwargs['plugin_list'] = Plugin.objects.all()
        return super(ListModule, self).get_context_data(**kwargs)


""" PLUGIN  """


class PluginCreate(CreateView):
    model = Plugin
    template_name = 'Plugin/form_create_plugin.html'
    form_class = PluginForm
    success_url = "/server/plugin/"

    def form_valid(self, form):
        if self.request.method == 'POST':
            return super(PluginCreate, self).form_valid(form)
        return PermissionDenied


class PluginModify(UpdateView):
    model = Plugin
    template_name = 'Plugin/form_create_plugin.html'
    form_class = PluginForm
    success_url = "/server/plugin/"

    def form_valid(self, form):
        if self.request.method == 'POST':
            return super(PluginModify, self).form_valid(form)
        raise PermissionDenied


class PluginList(ListView):
    model = Module
    template_name = 'Plugin/list_plugin.html'

    def get_context_data(self, **kwargs):
        kwargs['plugin_list'] = Plugin.objects.all()
        return super(PluginList, self).get_context_data(**kwargs)


""" Instruction  """


class InstructionCreate(CreateView):
    model = Instruction
    template_name = 'Instruction/form_create_instruction.html'
    form_class = InstructionsForm
    success_url = "/server/instruction/"

    def form_valid(self, form):
        if self.request.method == 'POST':
            return super(InstructionCreate, self).form_valid(form)
        return PermissionDenied


class InstructionModify(UpdateView):
    model = Instruction
    template_name = 'Instruction/form_create_instruction.html'
    form_class = InstructionsForm
    success_url = "/server/instruction/"

    def form_valid(self, form):
        if self.request.method == 'POST':
            return super(InstructionModify, self).form_valid(form)
        raise PermissionDenied


class InstructionList(ListView):
    model = Instruction
    template_name = 'Instruction/list_instruction.html'

    def get_context_data(self, **kwargs):
        kwargs['instruction_list'] = Instruction.objects.all()
        return super(InstructionList, self).get_context_data(**kwargs)


""" SERVICES  """


def job_receiver(request):
    if request.method == "POST":
        name = request.POST["name"]
        module = request.POST["module"]
        plugin = request.POST["plugin"]
        instruction = request.POST["instruction"]
        parameter = request.POST["parameter"]
        state = request.POST["state"]

        job = Job(name, module, plugin, instruction, parameter, "", state)
        # try:
        if (job.module == "SELF"):
            ip_module = "127.0.0.1:8000"
        else:
            ip_module = Module.objects.get(name=job.module).ip
        job.command = search_command(job)
        job.state = job.send_job(ip_module)
        # job.state = job.do_job()
        # send job
        return HttpResponse(job.state)


"""
        except:
            # Catch and create new exceptions
            return HttpResponse(job.error)
"""


def search_command(job):
    instruct = Instruction.objects.get(name=job.instruction)

    my_file = open('instructions.html', 'w')
    my_file.write(instruct.name)

    return instruct.command

    # Repair this

    """
    module = Module.objects.get(name=job.module)

    my_file = open('instructions.html', 'w')
    my_file.write(module.name + "--->" + job.module)
    my_file.write(Plugin.objects.filter(name=module.plugins))


    for plugin in module.plugins.all():
        my_file.write(plugin.name)
        for instruction in plugin.instructions.all():
            my_file.write(instruction.name)
            if instruction == job.instruction:
                return instruction.command

    my_file.close()
    # else raise exception
    """
