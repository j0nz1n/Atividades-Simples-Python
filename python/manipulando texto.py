frase = 'Curso em Vídeo Python'

print(frase[9:14:2]) #Mostra o que está no espaço 9 até o 13 da string de 2 em 2

print(len(frase)) #Informa o número de caracteres

print(frase.count('o', 0, 14)) #Informa quantos "o" tem na frase do espaço 0 ao 13

print(frase.find('deo')) #Informa quantas vezes tem "deo" na string

print('{}'.format('Curso' in frase)) #Informa se há ou não "Curso" na string

frase.replace('Python', 'Android') #Substitui a primeira informação pela segunda na string

frase.upper() #Deixa tudo maiúsculo

frase.lower() #Deixa tudo minúsculo

frase.capitalize() #Deixa só a primeira letra maiúscula

frase.title() #Deixa a primeira letra maiúscula em cada palavra

frase.strip() #Apaga os espaços no começo e no final da string

frase.rstrip() #Apaga os espaços no final da string

frase.lstrip() #Apaga os espaços no começo da string

frase.split() #Transforma cada palavra da string em uma lista separada

'-'.join(frase) #Junta tudo e acrescenta um "-" nos espaços

print("""PRINTA UM TEXTÃO""")
