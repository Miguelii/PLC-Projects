import re 
import json 

listadics = []
N=20
with open("processos.txt", "r") as fileoriginal:
    fileN = [next(fileoriginal) for x in range(N)]

for v in fileN: 
    lista = re.split(r'::|[ ]+[ ]+',v)
    dic = {}
    contador = 0 
    nome = 1 
    linha = 0 
    for elemento in lista: 
        if elemento != '\n' and elemento != '': 
            if contador == 0: 
                dic["numero processo"] = elemento
            elif contador == 1: 
                dic["data"] = elemento
            elif contador >= 2: 
                dic["nome(s)" + str(nome)] = elemento
                nome += 1
            contador += 1
    listadics.append(dic)
    
with open("json.json", 'w') as file:
    file.write((json.dumps(listadics, indent=4, sort_keys= False)))