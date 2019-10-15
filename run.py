import os
from subprocess import Popen
import webbrowser
import time

mlflow_port = 5002

Popen(f"cmd /c mlflow ui --port={mlflow_port}", shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

# give a sec till this start-up
time.sleep(1)

webbrowser.open(f"http://kubernetes.docker.internal:{mlflow_port}")

Popen("cmd /c jupyter notebook", shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
