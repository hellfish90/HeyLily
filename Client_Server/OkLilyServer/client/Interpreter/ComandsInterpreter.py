__author__ = 'Marc'

from abc import abstractmethod, ABCMeta
import serial
import requests
import threading
from Feedback import Cube_Led_Feedback

# Refactor

class Job(object):
    error = 3
    create = 0
    received = 1
    sent = 2
    success = 4

    Type_State = (
        (create, 'created'),
        (received, 'received'),
        (sent, 'sent'),
        (success, 'success'),
        (error, 'error')
    )

    def __init__(self, name, module, plugin, instruction, parameter, command, state):
        self.name = name
        self.module = module
        self.plugin = plugin
        self.instruction = instruction
        self.parameter = parameter
        self.command = command
        self.state = state


class CommandsInterpreter(object):
    __metaclass__ = ABCMeta

    def __init__(self, feedback):
        self.feedback = feedback

    @abstractmethod
    def get_job_by_stream_data(self, data):
        """return a Job Object with module, instruction, state=created and plugin"""
        raise NotImplementedError

    def send_job_to_server(self, job):

        # environment vars
        server = "127.0.0.1:8000"
        self_name = "lab_module"
        connection_error = "-1"
        print "Start sending job"

        if isinstance(job, Job):

            name = self_name + " to " + job.module + " orders do " + job.instruction + " on " + job.plugin

            payload = {'name': name, 'plugin': job.plugin,
                       'module': job.module, 'instruction': job.instruction,
                       'parameter': job.parameter, 'command': job.command,
                       'state': job.state}
            try:

                r = requests.post("http://" + server + "/server/job/receiver/", data=payload)
                callback = r.text

                if self.bad_response(r.text):
                    # if the response is bad
                    self.feedback.do_feedback(self.feedback.error)
                else:
                    # if the response is well
                    self.feedback.do_feedback(int(r.text))

            except:
                # if not response
                # Feedback
                callback = connection_error
                self.feedback.do_feedback(self.feedback.no_connection_with_server)
                # debug

        else:
            self.feedback.do_feedback(self.feedback.bad_job)
            callback = "-2"

        my_file = open('callback_sender.html', 'w')
        my_file.write(callback)
        my_file.close()

    def bad_response(self, response):
        return len(response) > 10


class EasyShieldCommandInterpreter(CommandsInterpreter):

    feedback_cube = Cube_Led_Feedback()

    def hear_user(self):

        ser = serial.Serial('/dev/ttyACM1', 9600)

        while 1:

            line = ser.readline()
            if line.find("COMMAND") != -1:
                job = self.get_job_by_stream_data(line)
                self.send_job_to_server(job)
            if line.find("CommandDetected") != -1:
                print line
                self.feedback_cube.do_feedback(self.feedback.received)
            if line.find("RESTART") != -1:
                print line
                self.feedback_cube.do_feedback(self.feedback.done)


def get_job_by_stream_data(self, data):
    data = data.split(';')
    plugin = data[1]
    module = data[2]
    instruction = data[3]
    parameter = data[4]

    return Job("", module, plugin, instruction, parameter, "", Job.create)


def test_send_command(self):
    job = Job("", "module", "test", "llistar", "1", "", Job.create)
    self.send_job_to_server(job)
