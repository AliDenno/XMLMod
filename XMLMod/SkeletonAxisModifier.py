import xml.etree.ElementTree as ET
import os
import zipfile
import time
import ChknOperations as Op

def alterAxis(FileName):    
    tree = ET.parse('NEW/Headless_'+FileName)
    root = tree.getroot()
    for j in root:
        if(j.tag=="BONE"):
            Val=j[0].text.split()
            j[0].text=str((float(Val[0])))+" "+str((float(Val[1])))+" "+str((float(Val[2])))
    tree.write("New/"+FileName)
    try:
        os.remove('NEW/Headless_'+FileName)
    except OSError:
        pass
    Op.writeHeadFullFile(FileName)

FileName='Ebzz9.xsf'
content=Op.readHeadfullFile(FileName)
Op.writeHeadlessFile(content,FileName)
alterAxis(FileName)
print("done")
