# MindRisers-Website-with-RASA
Getting Started with Rasa on Windows with VS Code
Rasa is an open source system for conversational AI. This tutorial outlines how to get started on Windows using Visual Studio Code.

Is this tutorial for you?
There are easier ways to install and initialize Rasa. I’ve had good success with Docker-Compose, for example — it’s quick and easy. However, Docker Desktop for Windows requires that the Hyper-V feature be enabled, which is a no-go for anyone using VirtualBox on the same machine, and while using Docker inside VirtualBox does work, it precludes you from using the host’s dedicated GPU for model training using Tensorflow.
If you’re in the same Docker/Hyper-V/VirtualBox predicament as I am, this tutorial provides an alternative without requiring Docker. If you don’t use VirtualBox and Docker runs fine on your host, you may not need this tutorial. In that case I recommend Rasa’s documentation for installation:
Overview of Steps
Install Python with MiniConda
Create a virtual environment for our Rasa project
Configure Visual Studio Code to use that virtual environment
Initialize a new Rasa project and train the default model
1. Install Python with MiniConda
Install MiniConda for Windows. This will include Python and Pip. The downloads can be found here:
https://docs.conda.io/en/latest/miniconda.html
Rasa requires Python 3 and is not compatible with Python 2, so download the installer for Python 3.7 and complete the setup process. If the installer gives the option to override the system PATH variable, I recommend against it, especially if you already have a system Python installation. MiniConda will keep things separate in that case, so there’s no need to overwrite the PATH variable, and in the following sections we’ll make sure VS Code is using the correct version of Python and its packages.
Python 3.8 is available at time of writing, but it Rasa’s dependencies (specifically Tensorflow) wouldn’t install for me unless I used Python 3.7. This is the main reason I used MiniConda to install Python 3.7. Your mileage may vary.
2. Create a virtual environment
After MiniConda is installed, we can create a virtual environment for our Rasa project which will help keep Python packages contained and versions constrained. This is preferable over globally installing packages.
Search for “Anaconda Prompt” in the Windows start menu. The name might come across as “Anaconda Prompt (miniconda3)”. Run it, which will open a command prompt. In the command line, run these commands:
conda create -n hellorasa python=3.7
conda activate hellorasa
pip install rasa
These commands will respectively create a new virtual environment named “hellorasa”, activate that environment for the current console session, and then install Rasa.
You can confirm the installation by running:
rasa --version
If it outputs the Rasa version, the installation was successful. Feel free to close Anaconda Prompt, because we’ll be configuring Visual Studio Code to use this environment which will allow you to run integrated terminals from inside the IDE moving forward, instead of using Anaconda Prompt.
3. Configure Visual Studio Code
If you don’t already have Visual Studio Code installed, you can download it here:
https://code.visualstudio.com/Download
Let’s configure the VS Code setting for Python. First, install this Python extension from Microsoft:
Python
A Visual Studio Code extension with rich support for the Python language (for all actively supported versions of the…
marketplace.visualstudio.com
You can also press Ctrl+Shift+X to open the extensions window, and search for Python. Restart VS Code after installing the extension.
Next, create a new empty folder on your computer and open it in VS Code. I called mine “HelloRasa”, but you can call it anything. We’ll be using this folder to contain the Rasa project files as well as some VS Code settings to set up paths for Python.
With the folder open in VS Code, press Ctrl+Shift+P and type “Python: Select Interpreter”. This should prompt you with a list of interpreters to select from. Select the one that matches the virtual environment you configured with Conda, which should be something like:
Python 3.7.7 64-bit ('hellorasa': conda)
This will configure the Python path in a file called .vscode/settings.json in the current folder. Open that file, because we’ll need to add a couple more settings to make the terminal work.
Edit .vscode/settings.json to set these three options:

{




 "python.pythonPath": "%HOMEPATH%\\miniconda3\\envs\\hellorasa\\python.exe",


 "terminal.integrated.shell.windows":"C:\\Windows\\System32\\cmd.exe",


 "terminal.integrated.shellArgs.windows": ["/K", "%HOMEPATH%\\miniconda3\\Scripts\\activate.bat %HOMEPATH%\\miniconda3\\envs\\hellorasa"]


}




You may need to replace instances of `%HOMEPATH%\\miniconda3` with the actual path to your MiniConda installation, and you may need to replace hellorasa with the name you chose for your virtual environment.
Restart VS Code again to apply these changes. Now you should be able to run a terminal from VS Code using Ctrl+Shift+` (Ctrl+Shift-Backtick), and doing so will automatically activate the virtual environment.
To verify that this worked, run the following commands in that terminal window:
python --version
conda --version
rasa --version
4. Initialize Rasa
Now that Python and Rasa are installed, it’s time to create a Rasa project. Make sure your “HelloRasa” folder is open in VS Code, open a terminal, and run:
rasa init
That’s it! The init command will prompt you with a few questions interactively. If you prefer, you could run rasa init --no-prompt instead, which will just use the defaults.
From here on, you’ll be able to use any other Rasa command, such as:
rasa train to train your model
rasa shell to talk to your Rasa bot

