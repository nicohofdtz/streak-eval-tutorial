# Tutorial: Correction and analysis of streak camera data with python in JupyerLab

This repository comprises Jupyter Notebooks that will help you getting started with the evaluation of streak images via Python.

## Installation

#### Prerequisites

Python >= 3.8.0
Git

#### Clone repository

Clone this repository to your desired workspace:

```
git clone https://github.com/nicohofdtz/streak-eval-tutorial.git
```

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

Install JupyterLab, Matplotplib

```
pip install jupyterlab matplotlib numpy pandas json-tricks import-ipynb
```

(WIP)

## Usage

#### Running JupyterLab

Run (when using pipenv run this from inside the shell):

```
jupyter lab
```

JupyerLab will usually open in a new tab in your standard web browser.
If it doesn't open automatically have a look at the console ouput for a line similar to

```
[I 09:18:53.839 LabApp] Jupyter Notebook 6.1.4 is running at:
[I 09:18:53.839 LabApp] https://YouComputerName:Port/
```

copy the given URL to a browser.
(WIP)
