# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 18:18:02 2018

A simple attendance program for FRC Team 6560 Charging Champions

@author: Albert Lin
"""

#%%
import os
import csv
import numpy as np

#%%
#checking if file of names exists
nameFile = 'AKNames.csv'
hasNameFile = False
for file in os.listdir():
    if file.__eq__(nameFile):
        hasNameFile = True
#if it does not, then create one and initialize
if not hasNameFile:
    print(nameFile + " not found, creating one...")
    newMembers = []
    done = False
    while not done:
        print("type in a member's name to add or type 'q' if done adding members")
        userIn = input().lower()
        if userIn.__eq__("q"):
            done = True
        else:
            newMembers.append(userIn)
            print(newMembers)
    with open(nameFile, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|')
        filewriter.writerow(newMembers)
#%%
#loading names from the csv file
with open(nameFile, 'r') as csvfile:
    reader = csv.reader(csvfile)
    names = []
    for name in reader:
        names.append(name)
    print(names)
    
