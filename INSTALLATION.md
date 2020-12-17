# Installation instructions

This document describes how to prepare your own PC for the first lecture of HiLASE 2021 Python course. 
It should take less than one hour to complete.
*Please, really do it and let us know if there are any complications.*

## Recommended: Installing Python using miniconda

This is our preferred way how to install Python for scientific computing as it seamlessly bundles required binary (even non-Python) packages
and works almost identically on all major platforms.

1. Download the Python 3.8 version of miniconda for your operating system from https://docs.conda.io/en/latest/miniconda.html.
2. Follow the "Regular installation" instructions in https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation.
On MacOS, run
```
bash Miniconda3-latest-MacOSX-x86_64.sh
```
On Linux:
```
bash Miniconda3-latest-Linux-x86_64.sh
```
On Windows, execute the downloaded `.exe` file.
3. Verify the installation.
   a. If you are unsure about things like environment variables etc., restart your system first.
   b. Open a terminal with conda initialized as described in https://conda.io/projects/conda/en/latest/user-guide/getting-started.html.
   c. Verify conda installation by running `conda --version`.
4. Create a dedicated virtual environment:
```
conda create -n python-course-2021 -c conda-forge python=3.8
```
5. Activate this new environment:
```
conda activate python-course-2021
```
6. Install required packages (always do this after activating the correct conda environment):
```
conda install numpy scipy matplotlib plotly pandas sphinx black pytest flake8 sqlalchemy xarray pep8-naming openpyxl lxml jupyter ipython
```

## Alternative: System Python in Ubuntu

If you are using a recent version of Ubuntu (say 20.04 LTS), you should have a recommended version of Python (3.8)
already installed on your system. In such case, just make sure you have the `python3.8-venv` and `python3.8-pip`
packages installed as well. You will need to work in a "virtual environment" to install the necessary libraries.

In a directory of your choice, run the following:

```
python3.8 -m venv ./python-course-venv       # Create the environment (once)
source ./python-course-venv/bin/activate     # Use the environment (every time)
```

(Note that we are using Python 3.8, the newest, non-default version 3.9 is not friendly with all the scientific libraries as of December 2020).

Then you can install the required libraries:

```
pip install wheel
pip install numpy scipy matplotlib plotly pandas sphinx black pytest flake8 sqlalchemy xarray pep8-naming openpyxl lxml jupyter ipython
```

## Verify the installation 

Please check that your local installation works by starting an ipython interactive session:
```
ipython
```
You should see something like
```
Python 3.8.6 | packaged by conda-forge | (default, Nov 27 2020, 19:17:44)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.19.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```
Try to run (maybe your first) Python minicode:
```
In [1]: import numpy

In [2]: print(f"My numpy version is {numpy.version.full_version}")
My numpy version is 1.19.4
```
(The numpy version can differ in case a newer version has been released since Dec 2020.)


## On-line alternative

**(In preparation)** We will use an on-line environment for presenting the code that you can observe, comment and even step in.
In extreme cases, you will even be able to live without local Python installation though it definitely is not recommended.
More details will follow.

## Further alternatives? Rather not.

We believe that basically any installation of relatively new Python (version 3.7 or higher) is capable of installing the requested
libraries and running the code we will show during the course but... the small "but" is in that there may be small glitches or inconsistencies
that would typically occur during the lecture when the time should be devoted to other topics. We simply cannot give support and you are on your own.
*(Please, let us know if you really really must work in an environment different from the abovementioned alternatives.)*

## Jupyter Notebooks

We will use the [Jupyter](https://jupyter.org/) Notebook environment, which is a web-based application that allows to run Python code
and combine it seamlesly with graphical output and user interaction. Notebooks thus enable creating and working with live documents.

Please try to start Jupyter Notebook server as described in https://jupyter.readthedocs.io/en/latest/running.html.
Play a little bit around with the [Notebook Basics](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html)

## Recommended development environments / editors

A capable, Python-aware editor or integrated development environment (IDE) becomes indispensable
once you start with a more "serious" development: larger projects, shared packages etc.
We have short-listed community and personally proven possibilities.

### Visual Studio Code

This is a general, multi-purpose and very capable free editor, not just for Python.

https://code.visualstudio.com/

### PyCharm

This is a heavy-weight, full IDE dedicated to Python, probably the most powerful one. Although there is a Professional version,
in scientific computing, with the Community edition you will be just fine.

https://www.jetbrains.com/pycharm/

## Notepad++, vim, emacs, ...

Many editors have at least some basic syntax highlighting for Python, so don't be afraid to use your favourite one.