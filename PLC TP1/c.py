import re

f = open("processos.txt")
linhas = f.readlines()
relacao = {}

for linha in linhas: 
    lista = re.split(r'::',linha)
    for elemento in lista: 
        new_text = re.findall(r'(?i)(\birma[o]?|\bsobrinh[oa]|\bavo|\bti[oa]|\bprim[oa]|\bpai|\bfilh[oa]|\bmae)([ ]+?[a-zA-Z]+[.,])?',elemento)
        if new_text:
            a = []
            for k in range(len(new_text)): 
                a.append(new_text[k][0])

            for palavra in a:
                por = palavra
                aux = list(por)
                if aux[len(aux)-1] == 's': 
                    del(aux[len(aux)-1])
                aux[0] = aux[0].upper()
                por = ''.join(aux[i] for i in range(len(aux)))

                if por not in relacao: 
                    relacao[por] = 1 
                else: 
                    relacao[por] += 1 
for rela in relacao: 
    print ("Relacao: " + rela + ": " + str(relacao[rela]))