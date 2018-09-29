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
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|')
        filewriter.writerow(newMembers)
#%%
#loading names from the csv file
with open(nameFile, 'r') as csvfile:
    reader = csv.reader(csvfile)
    names = []
    for row in reader:
        for name in row:
            names.append(name)
    print("Member List:", names)
#%%
# create a data file for each member if none exists yet
for name in names:
    hasFile = False
    dataFileName = name + ".csv"
    for file in os.listdir():
        if file.__eq__(dataFileName):
            hasFile = True
    if not hasFile:
        with open(dataFileName, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|')
            
print("Welcome to the Attendance Keeper!")

#%%
#defining actions

def signIn(self, name):
    
def signOut(self, name):
    
def show(self, name):
    
def add(self, name):
    
def remove(self, name):

#%%
#interactive session
running = True
while running:
    print("Sign (I)n / Sign (O)ut / (S)how Information / (A)dd Member / (R)emove Member / (Q)uit")
    mode = input().lower()
    if mode.__eq__('q'):
        running = False
    else:
        print("type in name or 'q' to quit")
        userIn = input().lower()
        if userIn.__eq__('q'):
            print("returning back to mode selection")
        else:
            if userIn in names:
                if mode.__eq__('i'):
                    signIn(userIn)
                elif mode.__eq__('o'):
                    signOut(userIn)
                elif mode.__eq__('s'):
                    show(userIn)
                elif mode.__eq__('a'):
                    add(userIn)
                elif mode.__eq__('r'):
                    remove(userIn)
            else:
                print("name not in list, returning to mode selection")
