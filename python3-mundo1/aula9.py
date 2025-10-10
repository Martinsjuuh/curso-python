frase ='Curso em Vídeo Python'
print(frase)

#Fatiamento
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print('oi')
print('''Olá,Tudo bem?Esse é um teste que pode printar esse texto todo com apenas 3 aspas.Vamos testar e vamos ver como vai ficar''')
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
#Análise
print(len(frase)) # Qual o tamanho da frase?
print(len(frase.strip())) # Remove espaços indesejado
#Transformação
print(frase.replace('Python','Android'))
print(frase)
print('Curso' in frase) # Se existe a palavra Curso na frase
print(frase.find('Curso')) # Posição
print(frase.lower().find('vídeo'))
print(frase.split()) #Criou uma lista com separador de espaço
#Divisão
dividido =frase.split()
print(dividido[0]) # Mostar só o curso
print(dividido[2] [3])
#Junção
'-'.join(frase)