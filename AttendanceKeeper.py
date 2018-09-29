# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 18:18:02 2018

A simple attendance program for FRC Team 6560 Charging Champions

@author: Albert Lin
"""

'''
config setup
'''
#%%
import os
import configparser
import numpy as np

#%%
print("Loading settings from local folder...")

config = configparser.ConfigParser()
config.selections()
