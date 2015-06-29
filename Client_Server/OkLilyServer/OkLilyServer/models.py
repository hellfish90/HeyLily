from django.db import models
import subprocess
import requests


class Job(models.Model):

    create = "0"
    received = "1"
    sent = "2"
    error = "3"
    success = "4"
    not_understand = "5"
    you_say_something = "6"
    fact = "7"
    doing = "8"
    tell_me = "9"
    no_connection_with_server = "11"
    bad_job = "12"

    Type_State = (
        (create, 'created'),
        (received, 'received'),
        (sent, 'sent'),
        (success, 'success'),
        (error, 'error')
    )

    name = models.CharField(max_length=50, verbose_name="name", default='no value')
    module = models.CharField(max_length=50, verbose_name="name_module", default='no value')
    plugin = models.CharField(max_length=50, verbose_name="plugin_name", default='no value')
    instruction = models.CharField(max_length=50, verbose_name="name_instruction", default='no value')
    parameter = models.CharField(max_length=50, verbose_name="parameter_instruction", default='no value')
    command = models.CharField(max_length=50, verbose_name="value_instruction_command", default='no value')
    state = models.IntegerField(choices=Type_State, default=create, verbose_name="command state")

    def __init__(self, name, module, plugin, instruction, parameter, command, state):
        self.name = name
        self.module = module
        self.plugin = plugin
        self.instruction = instruction
        self.command = command
        self.state = state
        self.parameter = parameter

    def do_job(self):

        try:

            
            my_file = open('/tmp/chanel', 'w')
            my_file.write(self.parameter)
            my_file.close()
            self.state = subprocess.check_output(str(self.command), shell=True)

            my_file = open('callback_proces.html','w')
            my_file.write(self.state)
            my_file.close()

        except Exception as e:
            my_file = open('callback_proces.html', 'w')
            my_file.write("State: "+self.state+" Error: "+self.command+"</p>"+ self.name + "state: " +self.state + "parameter:" + self.parameter + "Exception:" + e.message )
            my_file.close()
            self.state = "-1"

        if self.state != "-1":
            return self.success
        else:
            return self.error

    def send_job(self, ip):

        payload = {'name': self.name, 'plugin': self.plugin,
                   'module': self.module, 'instruction': self.instruction,
                   'parameter':self.parameter, 'command': self.command,
                   'state': self.state}

        my_file = open('command.html', 'w')
        my_file.write(self.command)
        my_file.close()


        try:
            r = requests.post("http://" + ip + "/client/job/receiver/", data=payload)
            callback = r.text

            if self.bad_response(r.text):
                # if the response is bad
                callback = r.text
            else:
                # if the response is well
                callback = r.text
            my_file = open('callback_send_job.html', 'w')
            my_file.write(callback)
            my_file.close()
            if len(callback) > 4:
                return "-1"
            else:
                return callback

        except Exception as e:

            my_file = open('callback_send_job.html', 'w')
            my_file.write("Error on send job")
            my_file.close()
            callback = e.message
            return "-1"

    def save_job_to_log(self):
        pass

    def bad_response(self, data):
        return len(data)>4
