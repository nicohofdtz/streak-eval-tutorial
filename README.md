# Tutorial: Correction and analysis of streak camera data with python in JupyterLab

_Note: This README aims to provide help for absolute python/programming novices. If you experience any issues or struggles please report (by creating an issue on GitHub or via email) so we can add the information you were missing._

This repository comprises Jupyter Notebooks that will help you to get started with the evaluation of streak images via Python. Code in gray boxes has to through a command-line interface (e.g. cmd on Windows). If you are unfamiliar with the basic concepts of command-line interfaces (especially navigation), read the first two items on [Digital Citizens' _11 basic commands you should know_](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands/)

## Installation

#### Prerequisites

###### Install Python

Go to [python.org](https://python.org) to download and install Python 3.8.6 (3.9 compatibility not tested).
Important: Go for the custom installation and check the "_Add Python to path_" or "_Add Python to environment variables_" option during installation to add python to your path. This allows to run python from the command-line without specifying the installation folder (`python` instead `C:\Users\username\AppData\Local\Programs\Python\Python38\python`).

###### Install Git

Go [git-scm.org](https://git-scm.org) to download and install Git.

#### Clone repository

If you're checking out/working with multiple software projects, having a dedicated _workspace_ folder for these helps to keep your system uncluttered. Since most command-lines will start in the user directory, that could be a reasonable location for that folder.
Navigate to your desired workspace folder and clone this repository by:

```
git clone https://github.com/nicohofdtz/streak-eval-tutorial.git
```

(enter or copy-paste to your command line and press enter)

#### Install dependencies

###### Method 1 - Using Pipenv:

Read [here](https://towardsdatascience.com/virtual-environments-for-data-science-running-python-and-jupyter-with-pipenv-c6cb6c44a405) why it's a good idea to use pipenv.
Having [Pipenv](https://github.com/pypa/pipenv) installed navigate to the project folder and run:

```
pipenv install
```

This automatically installs all required packages in a virtual environment.
After the installation is finished activate the project's virtual environment:

```
pipenv shell
```

Connect the environment to a kernel:

```
python -m ipykernel install --user --display-name streak-eval-tut-kernel --name streak-eval-tut-kernel
```

Make sure to select this kernel in JupyterLab.

###### Method 2 - Manual (global installations):

Install the streakimage package:

```
pip install git+https://github.com/nicohofdtz/streakimage#egg=streakimage
```

This package provides the python class that will import and hold the streak camera images

Install packages from pip:

```
pip install jupyterlab matplotlib numpy pandas json-tricks import-ipynb
```

Note: If you get a `ModuleNotFoundError: No module named 'module'`, the above list is most likely deprecated. Just run `pip install 'module'` to install the missing module!

## Usage

Open your command-line and navigate to the project folder.
When using pipenv, activate the shell.

```
pipenv shell
```

#### Running JupyterLab

Run:

```
jupyter lab
```

JupyterLab will usually open in a new tab in your standard web browser.
If it doesn't open automatically, have a look at the console output for a line similar to

```
[I 09:18:53.839 LabApp] Jupyter Notebook 6.1.4 is running at:
[I 09:18:53.839 LabApp] https://YouComputerName:Port/
```

and copy the given URL to a browser.

To the left you find a list of files.  
![Screenshot of the file browser in JupyteLab](https://github.com/nicohofdtz/streak-eval-tutorial/blob/main/blob/readme-jupyterlab-file-browser.png)  
Open the Jupyter Notebook (an .ipynb-file) you're interested in. When you open a notebook for the first time you will be asked to select a kernel for that notebook. Important: Select the kernel you created during the installation. Choosing another kernel may (and likely will) cause issues with installed packages.
The current kernel can be seen (and changed) on the top right of the notebook.  
![Screenshot of a notebok in JupyterLab](https://github.com/nicohofdtz/streak-eval-tutorial/blob/main/blob/readme-jupyterlab-actual-kernel.png)  
A notebook consists of blocks that can be executed step by step. Press Ctrl+Enter to execute the currently selected block or Shift+Enter to execute and advance to the next. The functionality of the blocks is thoroughly explained within the notebook.  
Feel free to experiment with the code. Take note that variables, functions, graphs etc. persist in memory unless they're explicitly deleted/closed or the kernel is shut down. If you're experiencing issues, try resetting your kernel with the reload button at the top of your notebook.
