import re

f = open("processos.txt")
linhas = f.readlines()

relacao = {}

for linha in linhas: 
    lista = re.split(r'::',linha)
    for elemento in lista: 
        new_text = re.search(r'([a-zA-Z]+[ ]?)+',elemento)
        if new_text: 
            texto = new_text.group() 
            if texto not in relacao: 
                relacao[texto] = 1 
            else: 
                relacao[texto] += 1 

for rela in relacao: 
    print ("Nome: " + rela + ": " + str(relacao[rela]))