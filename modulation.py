#TODO: Docstrings
import streamlit as st
import pandas as pd
import numpy as np 
import math
import matplotlib.pyplot as plt
from utils import awgn


class Modulation:


    def __init__(self,M):
        self.M = M # Size of signal constellation
        self.k = int(np.log2(M)) # Number of bits per symbol 
        # nbits = 3000        # Numer of bits to process
        # numSamplesPerSymbol = 1    # Oversampling factor


    def plot_constellation(self,signal=None):

        base_constellation_points = np.array([[-3,-3],[-3, -1], [-3, 1], [-3, 3],
                        [-1,-3],[-1, -1], [-1, 1], [-1, 3],
                        [1,-3],[1, -1], [1, 1], [1, 3],
                        [3,-3],[3, -1], [3, 1], [3, 3], ])

        # Create data
        baseline_area = np.pi*9
        baseline_color = 'black'
        
        # if signal argument is given, plot it before baseline signal,
        # So baseline points are over the signal ones, as points of
        # reference.
        if signal.any():
            signal_area = np.pi*3
            signal_color = (0,1,0)
            plt.scatter(signal[:,0],
                signal[:,1],
                s=signal_area, 
                c=signal_color,
                alpha=0.5,
                label= 'Signal')
    
        # To add other points than the base ones, just copy next line and change the input.
        plt.scatter(base_constellation_points[:,0],
            base_constellation_points[:,1],
            s=baseline_area, 
            c=baseline_color,
            alpha=0.5,
            marker='*',
            label= 'Baseline')
      
        # set the limits of the constellation axes
        axes = plt.gca() # gca = get current axes
        axes_limit = self.k + round(self.k*0.2)
        axes.set_xlim([- axes_limit, axes_limit])
        axes.set_ylim([- axes_limit, axes_limit])

        plt.title('{}-QAM  Constellation'.format(self.M))
        plt.xlabel('x')
        plt.ylabel('y')
        axes.legend()

        st.pyplot()
        # without using streamlit:
        # plt.show()
