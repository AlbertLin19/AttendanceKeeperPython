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
import time
#%%
#checking if file of names exists
nameFile = 'AKNames.csv'
hasNameFile = False
for file in os.listdir('.'):
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
    for file in os.listdir('.'):
        if file.__eq__(dataFileName):
            hasFile = True
    if not hasFile:
        with open(dataFileName, 'w') as csvfile:
            filewriter = csv.writer(csvfile)
            
print("Welcome to the Attendance Keeper!")

#%%
#defining actions

def signIn(name):
    timeIn = time.strftime("%H:%M:%S")[:5]
    date = time.strftime("%d/%m/%Y")
    fileName = name + '.csv'
    #checking if already signed in or not
    #loading entries
    with open(fileName, 'r') as csvfile:
        reader = csv.reader(csvfile)
        entries = []
        for row in reader:
            if row.__len__() != 0:
                entries.append(row)
    #checking if last entry is on same date
    sameDay = entries.__len__() != 0 and date.__eq__(entries[-1][0])
    
    #checking to see if you want to override
    if sameDay:
        print("There is already an entry - override? (y)es / (n)o")
        userIn = input().lower()
        if userIn.__eq__('y'):
            entries = entries[:-1]
            shouldInsert = True
        else:
            print("not signing in")
    else:
        shouldInsert = True
        
    #rewriting
    if shouldInsert:
        entries.append([date, timeIn])
        print("Signing " + name + " in at " + timeIn + " on " + date)
        with open(fileName, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|')
            for row in entries:
                filewriter.writerow(row)
def signOut(name):
    timeOut = time.strftime("%H:%M:%S")[:5]
    date = time.strftime("%d/%m/%Y")
    fileName = name + '.csv'
    #checking if already signed in or not
    #loading entries
    with open(fileName, 'r') as csvfile:
        reader = csv.reader(csvfile)
        entries = []
        for row in reader:
            if row.__len__() != 0:
                entries.append(row)
    #checking if last entry is on same date
    sameDay = entries.__len__() != 0 and date.__eq__(entries[-1][0])
    #checking if already signed out
    signedOut = entries.__len__() != 0 and entries[-1].__len__() > 2
    
    if not sameDay:
        print("you did not sign in yet for today")
        return
    if signedOut:
        print("you are already signed out - override? (y)es / (n)o")
        usrIn = input().lower()
        if not usrIn.__eq__('y'):
            print("not signing out")
            return
    print("Signing " + name + " out at " + timeOut + " on " + date)
    entries[-1] = [entries[-1][0], entries[-1][1], timeOut]
    with open(fileName, 'w') as csvfile:
        filewriter = csv.writer(csvfile)
        for row in entries:
            filewriter.writerow(row)
def show(name):
    fileName = name + '.csv'
    #loading entries
    with open(fileName, 'r') as csvfile:
        reader = csv.reader(csvfile)
        entries = []
        for row in reader:
            if row.__len__() != 0:
                entries.append(row)
    for row in entries:
        print(row)
    totalHrs, numAttendedMeetings = calcTotalHours(name = name)
    print("total hours: " + str(totalHrs))
    if numAttendedMeetings != 0:
        print("average hours spent at an attended meeting: " + str(totalHrs/numAttendedMeetings))
    print("rolling weekly attendance hour rate: " + str(totalHrs/weekNum))
def showAll():
    for name in names:
        print("showing: " + name)
        fileName = name + '.csv'
        #loading entries
        with open(fileName, 'r') as csvfile:
            reader = csv.reader(csvfile)
            entries = []
            for row in reader:
                if row.__len__() != 0:
                    entries.append(row)
        totalHrs, numAttendedMeetings = calcTotalHours(name = name)
        print("total hours: " + str(totalHrs))
        if numAttendedMeetings != 0:
            print("average hours spent at an attended meeting: " + str(totalHrs/numAttendedMeetings))
        print("rolling weekly attendance hour rate: " + str(totalHrs/weekNum))
        print()
def calcTotalHours(name):
    fileName = name + '.csv'
    hourCount = 0
    numAttendedMeetings = 0
    #loading entries
    with open(fileName, 'r') as csvfile:
        reader = csv.reader(csvfile)
        entries = []
        for row in reader:
            if row.__len__() != 0:
                entries.append(row)
    for row in entries:
        if row.__len__() == 3:
            startHr = int(row[1][:2])+int(row[1][3:5])/60
            endHr = int(row[2][:2])+int(row[2][3:5])/60
            hourCount+= endHr - startHr
            numAttendedMeetings += 1
    return hourCount, numAttendedMeetings
#%%
#interactive session
weekNum = 1
running = True
while running:
    print("sign (i)n / sign (o)ut / (s)how information / show (a)ll / set (w)eek / (q)uit")
    mode = input().lower()
    if not mode.__eq__('i') and not mode.__eq__('o') and not mode.__eq__('s') and not mode.__eq__('a') and not mode.__eq__('w') and not mode.__eq__('q'):
        print("not an available option, returning to option selection")
    elif mode.__eq__('q'):
        running = False
    elif mode.__eq__('a'):
        showAll()
    elif mode.__eq__('w'):
        print("week number currently at: " + str(weekNum))
        print("enter new week number")
        userIn = input()
        if userIn.isdigit():
            weekNum = int(userIn)
    else:
        print("type in name or 'q' to quit")
        userIn = input().lower()
        if userIn.__eq__('q'):
            print("returning back to mode selection")
        else:
            if userIn in names:
                if mode.__eq__('i'):
                    signIn(name = userIn)
                elif mode.__eq__('o'):
                    signOut(name = userIn)
                elif mode.__eq__('s'):
                    show(name = userIn)
            else:
                print("name not in list, returning to mode selection")
