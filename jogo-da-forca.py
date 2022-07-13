import random
from palavras import palavras

def palavra_valida(palavras):
    palavra = random.choice(palavras)  #esse comando vai fazer a escolha das palavras aleatoriamente
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)

    return palavra.upper()

def forca():
    palavra = palavra_valida(palavras)
    letras = set(palavra)  # letras das palavras




