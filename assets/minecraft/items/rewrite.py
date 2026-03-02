import json
import os

base_file_path = "assets/minecraft/items/apple.json"

with open(base_file_path,"r") as apple:
    data = json.load(apple)


for i in range(0,len(data['overrides'])):
    filepath = data['overrides'][i]['model']
    filename = os.path.basename(filepath)


    filepath2 = filepath + ".json"

    test = os.path.join("C:\\Users\\Minec\\AppData\\Roaming\\.minecraft\\resourcepacks\\RCMP RESOURCE PACK\\assets\\minecraft\\items\\",filepath2[5:])
    test = os.path.normpath(test)
    test = os.path.split(test)

    if not os.path.exists(test[0]):
        os.makedirs(test[0])

    file = open((test[0]+"\\"+test[1]),"w")
    
    temp = f'{{"model":{{"type":"model","model":"minecraft:{filepath}"}}}}'
    file.write(temp)
    file.close

    #print(filename,filepath,sep="        ")
