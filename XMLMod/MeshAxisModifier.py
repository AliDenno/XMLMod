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

def alterAxis(FileName):    
    tree = ET.parse('NEW/Headless_'+FileName)
    root = tree.getroot()
    for i in root:
        for j in i:
            #print (j.tag)
            if(j.tag=="VERTEX"):
                Val=j[0].text.split()
                j[0].text=str((float(Val[0])))+" "+str((float(Val[1])))+" "+str((float(Val[2])))
    tree.write("New/"+FileName)
    try:
        os.remove('NEW/Headless_'+FileName)
    except OSError:
        pass
    writeHeadFullFile(FileName)

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
    

FileName='93742.xmf'
content=readHeadfullFile(FileName)
writeHeadlessFile(content,FileName)
alterAxis(FileName)
print("done")
