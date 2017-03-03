import xml.etree.ElementTree as ET
import os
import zipfile
import time

def showFile(file):
    for line in file:
        print(line)

def readHeadfullFile(FileName):
    with open(FileName) as f:
        content = f.readlines()
    global Header
    Header = content[0]
    content[0] = ""
    return content

def writeHeadlessFile(content,FileName):
    thefile = open('NEW/Headless_'+FileName, 'w')
    for item in content:
        thefile.write("%s" % item)
    thefile.close()


def writeHeadFullFile(FileName):
    with open('NEW/'+FileName) as f:
        content = f.readlines()
    content=[Header]+content
    try:
        os.remove('NEW/'+FileName)
    except OSError:
        pass
    thefile = open('NEW/'+FileName, 'w')
    for item in content:
        thefile.write("%s" % item)
    thefile.close()
    