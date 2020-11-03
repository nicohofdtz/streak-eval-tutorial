# Tutorial: Correction and analysis of streak camera data with python in JupyerLab

This repository comprises Jupyter Notebook that will help you getting started with the evaluation of streak images via Python.

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

Having [Pipenv](https://github.com/pypa/pipenv) installed navigate to the project folder and run:

```
pipenv install
```

This should automatically install all required packages in a virtual environment.

###### Method 2 - Manual (global installations):

Install the streakimage package:

```
pip install git+https://github.com/nicohofdtz/streakimage#egg=streakimage
```

This package provides the python class that will import and hold the streak camera images

Install JupyterLab, Matplotplib

```
pip install jupyterlab, matplotlib
```

(WIP)

## Usage

#### Running JupyterLab

If using pipenv run

```
pipenv shell
```

Then run (if not using pipenv start here):

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
