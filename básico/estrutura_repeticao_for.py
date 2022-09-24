texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

    # função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ") 
    # end para deixar lado a lado