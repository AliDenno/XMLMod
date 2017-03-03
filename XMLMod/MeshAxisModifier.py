import xml.etree.ElementTree as ET
import os
import zipfile
import time
import ChknOperations as Op

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
    Op.writeHeadFullFile(FileName)
'''
FileName='93742.xmf'
content=Op.readHeadfullFile(FileName)
Op.writeHeadlessFile(content,FileName)
alterAxis(FileName)
print("done")
'''

files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(".xmf")]
for i in files:
    FileName=i
    #FileName='93742.xmf'
    content=Op.readHeadfullFile(FileName)
    Op.writeHeadlessFile(content,FileName)
    alterAxis(FileName)
    print("done")
