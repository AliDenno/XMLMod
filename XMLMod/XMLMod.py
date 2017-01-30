import xml.etree.ElementTree as ET
import os
import zipfile

def readArchive(filename):
    with zipfile.ZipFile(filename) as z:
        for filename in z.namelist():
            print filename

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


readArchive('bd.chkn')

'''
with zipfile.ZipFile('bd.chkn') as z:
    for filename in z.namelist():
        if not os.path.isdir(filename):
            # read the file
            with z.open(filename) as f:
                for line in f:
                    print line
'''


'''
tree = ET.parse('country_data.xml')
root = tree.getroot()
'''
