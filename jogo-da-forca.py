import random
from palavras import palavras
import string

def palavra_valida(palavras):
    palavra = random.choice(palavras)  #esse comando vai fazer a escolha das palavras aleatoriamente
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)

    return palavra.upper()

def forca():
    palavra = palavra_valida(palavras)
    letras = set(palavra)  # letras das palavras
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()   #o que o usuário adivinhou

    # #pegando o input do usuário







