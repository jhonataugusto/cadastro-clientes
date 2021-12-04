from os import replace

numeros = set()
numeros = {0}
arquivo = open('numeros.txt','a')

looping = True

while looping == True:

    texto = input('Digite o número desejado : ')
    numeros.add(texto)

    for numero in numeros:

        #parar o looping
        if texto == 'sair':

            looping = False
            break

        elif numero == texto:

            numeroConvertido = texto.replace('\t','')
            resultado = (numeroConvertido + ',')
            arquivo.writelines('55' + resultado  + '\n')
        
    
        
    

       
