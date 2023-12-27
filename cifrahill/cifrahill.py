# CIFRA DE HILL - Gustavo Souza Martins
import numpy as np
import sys

# GUIA PARA EXECUCAO:
# CIFRAR TEXTO CLARO >> py cifrahill.py -enc arquivoentrada.txt arquivosaida.txt
# DECIFRAR TEXTO CIFRADO >> py cifrahill.py -dec arquivoentrada.txt arquivosaida.txt
comando = sys.argv[1]
arquivoEntrada = sys.argv[2]
arquivoSaida = sys.argv[3]

# a chave deve conter 9 caracters para realizar a transformacao em uma matriz 3 por 3
# ao alterar a chave deve-se alterar tambem a variavel mKeyInv, visto que
# mKeyInv representar a matriz inversa modular da chave
key = "bbcdefghi"
# vale lembrar que a matriz que essa chave se torna nao pode ser uma matriz com
# determinante igual a zero, visto que nao é possivel obter a matriz inversa modular
# por exemplo, a chave "abcdefghi" não é uma chave possível

# matriz inversa (mod 127) calculada no site dcode.fr/matrix-inverse(data de acesso: 22/10/2022)
# cheguei na conclusao que implementar o calculo dessa matriz seria inviavel
# para o trabalho aqui realizado, visto que fugiria um pouco do proposito de mostrar
# a cifra de hill
mKeyInv = np.array([[1, 125, 1],[125, 96, 32],[1, 75, 52]])


# estendendo a string caso a divisao em bloco de 3 dela nao seja possivel
# como exemplifica no documento disponibilizado pelo professor
# optei por estender o texto com a letra g
def estenderEntrada(msgEntrada):
    while (len(msgEntrada) % 3)  != 0:
        msgEntrada += 'g'
        msgLen = len(msgEntrada)
    return msgEntrada


# funcao que transforma a chave em uma matriz 3 por 3 com os caracters em ascii
def mKeyAscii(key):
    asciiKey = np.array([ord(char) for char in key])
    mKey = asciiKey.reshape(3, 3)
    return mKey

# funcao para criptografar a mensagem de entrada, recebe 3 parametros:
# o texto claro, inteiro n que correponde ao indice ixj da matriz da chave
# para os valores definidos aqui n = 3
# esse inteiro n sera a divisao do texto claro em blocos, no caso de n = 3
# o texto claro sera dividido em blocos de 3 caractere
# e a chave de encriptacao
def enc(arquivoEntrada, n, key, arquivoSaida):
    with open(arquivoEntrada, "r") as file:
        msgEntrada = file.read()
    msgEntrada = estenderEntrada(msgEntrada)

    mKey = mKeyAscii(key)
    msgLen = len(msgEntrada)
    encMatriz = []
    msgEntradaDiv = [msgEntrada[i:i+n] for i in range(0, msgLen, n)]

    for bloco in msgEntradaDiv:
        msgAscii = np.array([ord(char) for char in bloco]).reshape(len(bloco), 1)
        # print("mKey: ",mKey,"msAscii:" ,msgAscii)
        encBloco = (np.dot(mKey, msgAscii) % 127).reshape(-1)
        encBloco = encBloco.tolist()
        encMatriz.append(encBloco)

    encMatriz = sum(encMatriz, [])
    msgEnc = ''.join(str(chr(char)) for char in encMatriz)

    with open(arquivoSaida, "w") as file:
        file.write(msgEnc)

# funcao para decifrar a mensagem encriptada, com tres parametros analogos a funcao
# de encriptar, o primeiro é a mensagem encriptada, o segundo a divisao de caracterers
# que sera realaizada na mensagem e o terceiro a matriz inversa modular(mod 127)
# da matriz da chave
def dec(arquivoEntrada, n, mKeyInv, arquivoSaida):
    with open(arquivoEntrada, "r") as file:
        msgEnc = file.read()

    decMatriz = []
    msgLen = len(msgEnc)
    msgEncDiv = [msgEnc[i:i+n] for i in range(0, msgLen, n)]

    for bloco in msgEncDiv:
        msgAscii = np.array([ord(char) for char in bloco]).reshape(len(bloco), 1)
        decBloco = (np.dot(mKeyInv, msgAscii) % 127).reshape(-1)
        decBloco = decBloco.tolist()
        decMatriz.append(decBloco)
    decMatriz = sum(decMatriz, [])
    msgDec = ''.join(str(chr(char)) for char in decMatriz)

    with open(arquivoSaida, "w") as file:
        file.write(msgDec)

if(comando == "-enc"):
    enc(arquivoEntrada, 3, key, arquivoSaida)
elif(comando == "-dec"):
    dec(arquivoEntrada, 3, mKeyInv, arquivoSaida)
