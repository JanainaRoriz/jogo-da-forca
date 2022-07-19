import random
from palavras import palavras
import string

def get_palavra_valida(palavras):
    palavra = random.choice(palavras)  #esse comando vai fazer a escolha das palavras aleatoriamente
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)

    return palavra.upper()

def forca():
    palavra = get_palavra_valida(palavras)
    letras = set(palavra)  # letras das palavras
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()   #o que o usuário adivinhou

    # #pegando o input do usuário
    while len(letras) > 0:
        #letras usadas
        print('Você já usou essas letras: ', ' '.join(letras_usadas))

        lista_palavras = [letra if letra in letras_usadas else '-' for letra in palavra]
        print('Palavra atual: ', ' '.join(lista_palavras))

        user_letra = input('Adivinhe uma letra: ').upper()
        if user_letra in alfabeto - letras_usadas:
            letras_usadas.add(user_letra)
            if user_letra in letras:
                letras.remove(user_letra)

        elif user_letra in letras_usadas:
            print('Você já usou essa letra. Tente outra.')
        else:
            print('Caractere inválido. Por favor, tente novamente.')

    #chega aqui quando len(letras) == 0







