__author__ = 'Marc'

from ComandsInterpreter import EasyShieldCommandInterpreter
from Feedback import Easy_VR_Feedback

if __name__=="__main__":

    feedback = Easy_VR_Feedback()
    interpreter = EasyShieldCommandInterpreter(feedback)
    interpreter.test_send_command()
