nome = "JoNaS"

print(nome.upper())    #todas maiusculas
print(nome.lower())    # todas minusculas
print(nome.title())     # 1º maiuscula

texto = "  Olá Mundo!    "

print(texto + '.')
print(texto.strip()+ '.')
print(texto.rstrip()+ '.')
print(texto.lstrip()+ '.')

menu = "Python"

print("####"+ menu + "####")
print(menu.center(14))
print(menu.center(14, '#'))


print('-'.join(menu))