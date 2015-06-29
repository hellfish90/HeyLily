#! /bin/bash

python Client_Server/OkLilyServer/manage.py runserver 0.0.0.0:8000 &
python Client_Server/OkLilyServer/client/Interpreter/run_interpreter.py &
