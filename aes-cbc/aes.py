# AES-CBC - Gustavo Souza Martins
import sys
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# a chave aceita somente os tamanhos 16, 24 e 32 bytes
arquivo = sys.argv[1]
chave = sys.argv[2]
iv = b"isso e um vetIni"

# passando a chave para bytes(tendo em mente que ela foi recebida como string)
chave = str.encode(chave)

with open(arquivo, "rb") as file:
    info = file.read()

# utilizo a chave como vetor de inicialização para que os vetores nao sejam aleatorios, fazendo com que o texto cifrado mude
# porme o terceiro parametro apresentado na proxima linha se refere ao vetor de inicialização(iv), que deve ser imprevisivel
# para adversarios
aesObj = AES.new(chave, AES.MODE_CBC, iv)
cifrado = aesObj.encrypt(pad(info, AES.block_size))

with open("arquivocifrado", "w") as file:
    file.write(b64encode(cifrado).decode("utf-8"))
