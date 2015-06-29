from django.views.generic import CreateView
from rest_framework.exceptions import PermissionDenied
from client.forms import *
from OkLilyServer.models import *
from django.http import HttpResponse
# Create your views here.


class JobReceiver(CreateView):
    model = Job
    template_name = 'Job/form_create_job.html'
    form_class = JobForm
    success_url = "/client/job"

    def form_valid(self, form):
        if self.request.method == 'POST':
            return super(JobReceiver, self).form_valid(form)
        return PermissionDenied


def job_receiver(request):
    if request.method == "POST":
        name = request.POST["name"]
        module = request.POST["name"]
        plugin = request.POST["plugin"]
        instruction = request.POST["instruction"]
        parameter = request.POST["parameter"]
        command = request.POST["command"]
        state = request.POST["state"]

        job = Job(name, module, plugin, instruction, parameter, command, state)
        job.state = job.do_job()
        job.save_job_to_log()

        my_file = open('callback_client.html', 'w')
        my_file.write(job.state)
        my_file.close()

        return HttpResponse(job.state)
