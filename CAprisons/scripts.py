"""
This script is written to create a widget for use in Lecture_1.ipynb.
"""

import pandas as pd
from datascience import *
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

import ipywidgets as widgets
plt.style.use('fivethirtyeight')

###

data= Table().read_table("data/data_for_widget.csv")
grouped = data.group(["institution_name", "year"], sum)

new_percents = grouped.column("total_population sum") / grouped.column("designed_capacity sum") * 100
grouped = grouped.with_column("Percent Occupied", new_percents)

institutions = grouped.group(0).column(0)
institutions

inp = widgets.IntSlider(
    value=0,
    min=0,
    max=39,
    step=1,
    description='Institution:',
    orientation='horizontal',
    readout= True,
    readout_format='d'
)

def f(inp):
    inst = grouped.where(0, institutions[inp])
    inst.plot(1, "Percent Occupied")
    year1 = inst.column("year") 
    if np.any(year1 == 2011):
#         plt.axvline(x=2011, color = "red")
        point1 = inst.where("year", 2011).column("Percent Occupied").item(0)
        plt.plot([2011], [point1], 'ro')
        
        plt.annotate("(2011, {0}%)".format(round(point1, 2)),
        xy=(2011, round(point1, 2)), xytext=(-15, 0),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='red', alpha=0.3),
        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
        
    if np.any(year1 == 2013):
#         plt.axvline(x=2013, color = "cyan")
        point2 = inst.where("year", 2013).column("Percent Occupied").item(0) 
        plt.plot([2013], [point2], 'co')
        
        plt.annotate("(2013, {0}%)".format(round(point2, 2)),
        xy=(2013, round(point2, 2)), xytext=(35, 20),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='cyan', alpha=0.3),
        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
        
    if np.any(year1 == 2014):
#         plt.axvline(x=2014, color = "orange")
        point3 = inst.where("year", 2014).column("Percent Occupied").item(0)
        plt.plot([2014], [point3], 'yo')
        
        plt.annotate("(2014, {0}%)".format(round(point3, 2)),
        xy=(2014, round(point3, 2)), xytext=(120, 15),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='orange', alpha=0.3),
        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
        
        
    plt.title(institutions[inp])
    
out = widgets.interactive_output(f, {'inp': inp})