"""
name = str(input("Ingresa tu nombre "))

texto_usuario = str(input("Ingresa un texto de mínimo de 10 caracteres "))

while len(texto_usuario) < 10 :
    print("Ingresa un texto con el número de caracteres necesarios")
    break
"""    

def count_letters(string):
    counter = 0
    for i in range(0,len(string)):
        if string[i].isalpha():
            counter += 1
    return counter


def count_words(text):
    counter = 1
    for i in range(0, len(text)):
        if text[i].isspace():
            counter += 1
    return counter

print(count_words("Hello, my name"))