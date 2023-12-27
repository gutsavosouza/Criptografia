# INSTRUÇÕES DE USO: **aes.py**

**1.** Instação da blibioteca *pycryptodome*

>`pip install pycryptodome`

**2.** Guia para rodar o código
- Basta executar o arquivo **aes.py** no terminal
- A linha de comando aceita dois parâmetros:
    - O primeiro é se refere ao local do arquivo à ser criptografado
    - O segundo é chave de criptografia que será utilizada no processo, essa chave possui uma limitação: só pode ser de 16, 24 e 32 bytes. Qualquer tamanho de chave diferente desses três vai fazer com que ocorra um erro
- O código por si só já executa o AES em modo CBC
- A saída do código é passada para um arquivo, criado no mesmo diretório em que foi executado, que contém a informação criptografada

**3.** Observação sobre o código
- O vetor de inicialização é definido como constante dentro do código, para não gerar inconstância no texto cifrado
