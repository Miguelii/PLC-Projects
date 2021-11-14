import json
import re

''' 

"CommentThread" : [
{
    "Processo" : "582",
    "Data" : "1909-05-12",
    "Nomes" : "Abel Almeida","Antonio Manuel Almeida", "Teresa Maria Sousa"
    },
    
''' 

def d():
    N=20
    with open("processos.txt", "r") as fileoriginal:
        fileN = [next(fileoriginal) for x in range(N)]

    d = []
    for v in fileN:
        l = v.split(' :: ')
        print(l)
        d.append(dict(s.split(':',1) for s in l))


    with open("json.json", 'w') as file:
        file.write((json.dumps(d, indent=4, sort_keys= False)))



d()
