import xml.etree.ElementTree as ET
import os
import zipfile

def readMesh(filename):
    print("Processing "+filename)
    tree = ET.parse(filename)
    root = tree.getroot()


# Read files in an archive
def readArchive(filename):
    count=0
    with zipfile.ZipFile(filename) as z:
        for filename in z.namelist():
            if filename.endswith(".xmf"):
              count+=1  
              readMesh(filename)

def parse(heatmap_dump,filename):

    #start_time = time.time()
    

    #tree = ET.parse('testxml.xml')
    tree = ET.parse(filename)
    root = tree.getroot()

    #print(root[1][0][1].text)
    #print(root[1][0].attrib['size'])
    #print(len(root[1][0]))

    for i in range(0,len(root)):
        #print("{0}:{1}".format(root[i].attrib['name'],root[i].attrib['pid']))
        process=pr.Process(root[i].attrib['name'],root[i].attrib['pid'])
        #print("add process: "+process.name)
        heatmap_dump.processes.append(process)
        for j in range(0,len(root[i])):
            #print("--------{0}:{1}".format(root[i][j].attrib['name'],root[i][j].attrib['base']))
            module=mod.Module(root[i][j].attrib['name'],root[i][j].attrib['base'],root[i][j].attrib['size'])
            heatmap_dump.processes[i].modules.append(module)
            for k in range(0,len(root[i][j])):
                #print("----------------{0}".format(root[i][j][k].text))
                tpage=pge.Page(root[i][j][k].text,root[i][j][k].attrib['Asci'],root[i][j][k].attrib['NAsci'],root[i][j][k].attrib['Num'],root[i][j][k].attrib['Ent'])
                heatmap_dump.processes[i].modules[j].pages.append(tpage)

    return heatmap_dump


#readArchive('bd.chkn')
archive = zipfile.ZipFile('bd.chkn', 'r')
mesh=archive.read('50.xmf')
#print(mesh)
'''
tree = ET.parse('xmltest.ki')
root = tree.getroot()
print(root.tag)
'''
'''
with open('50.xmf', 'r') as f:
    first_line = f.readline()
    print (first_line)
'''
text=''
with open('50.xmf') as f:
    text=f.readlines()
#print(type(text))
#print(text)
#Try to read the mesh without the header -> IT is messing up the element Tree 

'''
with zipfile.ZipFile('bd.chkn') as z:
    for filename in z.namelist():
        if not os.path.isdir(filename):
            # read the file
            with z.open(filename) as f:
                for line in f:
                    print line
'''
import time


tree = ET.parse('NewTestCase.xmf')
root = tree.getroot()
#print(len(root[0]))
#print(root[0][1].tag)

for i in root:
    for j in i:
        #print (j.tag)
        if(j.tag=="VERTEX"):
            Val=j[0].text.split()
            j[0].text=str((float(Val[0])))+" "+str((float(Val[1])))+" "+str((float(Val[2])+5000))
tree.write('T2.xml')
print("done")
time.sleep(5)
count =0
for i in root[0]:
    if(i.tag=="VERTEX"):
        Val=i[0].text.split()
        Val[1]=float(Val[1])+500
        i[0].text=str((float(Val[0])+500))+" "+str((float(Val[1])+500))+" "+str((float(Val[2])+500))
        #print(i.tag," ",i[0].text.split())
tree.write('T2.xml')

'''
for i in range(0,len(root[0])-1):

    if (root[0][1].tag=="VERTEX"):
        print(root[0][i][0].text.split())
    else:
        break
'''
#