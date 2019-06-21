#!/usr/bin/python3
import matplotlib.pyplot as plt
from numpy.random import rand
import pandas


#------------------scipy-------------------
# https://www.scipy.org/
# SciPy (pronounced “Sigh Pie”) is a Python-based ecosystem of open-source software for mathematics, science, and engineering. 


#------------------matplotlib-------------------
# https://matplotlib.org/
# Matplotlib is a Python 2D plotting library which produces publication quality figures in 
# a variety of hardcopy formats and interactive environments across platforms. 
# Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, 
# web application servers, and four graphical user interface toolkits.
#
# You'll need following matplotlib functions:
# --> scatter()


#--------------------numpy----------------------
# https://www.numpy.org/
# NumPy is the fundamental package for scientific computing with Python. It contains among other things:
#     a powerful N-dimensional array object
#     sophisticated (broadcasting) functions
#     tools for integrating C/C++ and Fortran code
#     useful linear algebra, Fourier transform, and random number capabilities
# Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. 
# Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.
#
# You'll need following numpy functions:
# --> rand()


#--------------------pandas----------------------
# https://pandas.pydata.org/
# pandas is an open-source Python library that provides high performance data analysis tools and easy to use data structures. 
# pandas is available for all Python installations, but it is a key part of the Anaconda distribution and works extremely well in Jupyter notebooks to share data, 
# code, analysis results, visualizations, and narrative text.
#
# You'll need following pandas functions:
#--> read_csv
#--> to_csv
#--> dataFrames
#--> informations about dataframes https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm


# *************Exercise***************
#
# Look at the example Plot from Matplotlib
# https://matplotlib.org/gallery/lines_bars_and_markers/scatter_with_legend.html#sphx-glr-gallery-lines-bars-and-markers-scatter-with-legend-py

# Group A: 
#   in the current file create a function "createData(data_points,filename)" that takes two arguments
#   int       data_points = "number of datapoints e.g. 250"
#   string    filename = "a filename e.g. scatterPlot.csv"
#   this function should create the specified number of datapoints suitable to be consumed for the scatterplot from the example above 
#   and write this date to a csv file named like the second argument in the current folder

# Group B: 
#   in the current file create a function "createPlot(filename)" that takes one argument
#   string    filename = "a filename e.g. scatterPlot.csv"
#   this function should read a csv file named 'filename' from the current folder and create a scatterplot like in the example above