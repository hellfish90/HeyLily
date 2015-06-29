__author__ = 'Marc'

from abc import abstractmethod, ABCMeta
import serial
import time

class Feedback(object):

    create = "0"
    received = "1"
    sent = "2"
    error = "3"
    success = "4"
    not_understand = "5"
    you_say_something = "6"
    done = "7"
    doing = "8"
    tell_me = "9"
    no_connection_with_server = "11"
    bad_job = "12"

    @abstractmethod
    def do_feedback(self, feedback):
        pass


class Easy_VR_Feedback(Feedback):

    def do_feedback(self, feedback):

        if feedback == self.not_understand:
            print "Not Understand"

        if feedback == self.you_say_something:
            print "You say something"

        if feedback == self.done:
            print "Done"

        if feedback == self.doing:
            print "doing"

        if feedback == self.tell_me:
            print "tell me"

        if feedback == self.error:
            #Do something more
            ser = serial.Serial('/dev/ttyACM1', 9600)
            cube = serial.Serial('/dev/ttyACM0',9600)
            cube.write("2")
            ser.write("1")
            time.sleep(0.5)
            cube.write("3")
            print "something are wrong"

        if feedback == self.no_connection_with_server:
            print "no connection whit server"


class Cube_Led_Feedback(Feedback):

    def do_feedback(self, feedback):

        if feedback == self.received:
            cube = serial.Serial('/dev/ttyACM0', 9600)
            cube.write("1")

        if feedback == self.you_say_something:
            print "You say something"

        if feedback == self.done:
            cube = serial.Serial('/dev/ttyACM0', 9600)
            cube.write("1")
            time.sleep(0.5)
            cube.write("3")
            print "Done"

        if feedback == self.doing:
            print "doing"

        if feedback == self.tell_me:
            print "tell me"

        if feedback == self.error:

            print "something are wrong"

        if feedback == self.no_connection_with_server:
            print "no connection whit server"