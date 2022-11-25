import os
import requests
import json
from pathlib import Path

# global variables
url =""
host =""
token =""
cookies = {'token': token}

carpeta ="Dump_Permisos/"

header={
    "header":"dsa",
    "Cookie":"token="+token,
    "Content-Type":"application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/json",
    # "Content-Length": 15,
    "Origin": "",
    "Referer": "",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Te": "trailers",
   
    
}

method ="POST"

# 201 no trae info

def test(id):
    # print(cookies)
    param ={
        "id_grupos":id
    }
    if method =="POST":
        r = requests.post(host+url, json=param,cookies=cookies)
    else:
        r = requests.get(host+url, data=param,cookies=cookies)
        
    # print(r.text)
    data = r.text.replace("\\","")
    data = data.replace('"{',"{")
    data = data.replace('}"',"}")
    exportData(data,carpeta+"data_id_{}".format(id))

def exportData(testData,nameFile):
    # print(testData)
    ruta = 'dump/{}.json'.format(nameFile)
    print(ruta)
    fle = Path(ruta)
    fle.touch(exist_ok=True)
    lenData = len(testData)
    # print(len(testData))
    # json_object = json.load(testData)
    # open("dump/permisos.json", 'x').close()
    with open(fle, "w") as outfile:
        outfile.write(testData)
        # print("exportado")
    

for i in range(11):
    test(i)