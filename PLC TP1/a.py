import re

f = open("processos.txt")
linhas = f.readlines()
datas = {}

for i in linhas:
    new_text = re.search(r'([0-9]+)::([0-9]{4})', i)
    if new_text:
        data = new_text.group(2)
        processo = new_text.group(1)
        if (data,processo) not in datas: 
            datas[(data,processo)] = 1 
        else: 
            datas[((data,processo))] += 1 
f.close()
for (a,b) in datas: 
    print("No ano " + str(a) + ", o processo " + str(b) + " aconteceu " + str(datas[a,b]) + " vezes")
  
