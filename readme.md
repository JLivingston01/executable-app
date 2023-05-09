## Python Executable with .venv on Windows

This project is a python executable on Windows that runs an integrated Flask/Dash project locally, and takes you to the browser.

### To run

These instructions are for Windows machines running git bash. Mac instructions will require some modifications. 

1. Create .venv in directory
2. Activate .venv
3. Upgrade pip
4. Install requirements.txt into the venv
5. Call pyinstaller on launcher.py to create launcher.exe as a one-file executable
6. Copy the executable into the working directory

```
python -m venv .venv
source .venv/scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pyinstaller --onefile launcher.py
cp dist/launcher.exe launcher.exe
```

You can now navigate in the explorer to your executable-app/launcher.exe executable, double-click, and the flask development server will launch the application, and your browser will open to 127.0.0.1:5001.