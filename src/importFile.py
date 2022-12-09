"""
Function to import any file from 'src' directory
"""
import os

def importFileAsTXT(filename, sanitise=False):
    text = "" 
    with open(filename,"r") as inputfile:
        text = inputfile.read()
    return text

def readme():
    print("importFileAsTXT(<FILENAME>, SANITISE=<BOOLEAN>)")
    print("returns a text")
