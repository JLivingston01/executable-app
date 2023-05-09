import os
import webbrowser
import time
import threading



#venv_dir = os.path.join(os.getcwd(), '.venv')
#activate_path = os.path.join(venv_dir, 'Scripts', 'activate.bat')
#os.system(f'"{activate_path}"')

activate_path = os.path.join('.venv', 'Scripts', 'activate.bat')
pypath = os.path.join('.venv', 'Scripts', 'python.exe')

def start_server():
    os.system(f'call "{activate_path}" && {pypath} wsgi.py')

thread = threading.Thread(target=start_server)
thread.start()

time.sleep(3)  # wait for the server to start up
webbrowser.open_new_tab("http://localhost:5001")