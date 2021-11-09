import re
from collections import defaultdict, Counter

# Calcula a frequência de processos por ano (primeiro elemento da data);

def a(): 
    file = open("processos.txt", "r")
    #print(file.read())

    #procurar o nr do processo e data
    processo = re.findall(r'[0-9]{3}::1[0-9]{3}', file.read())
    #print(processo)

    counts = defaultdict(Counter)
    for v,k in map(lambda s: s.split('::'), processo):
        counts[k][v] += 1
    for k,c in counts.items():
        s = ', '.join(f'Processo {k2} ocorreu {v2} vezes' for k2,v2 in c.items())
        print(f'Ano {k}: {s}')

    file.close()


a()



