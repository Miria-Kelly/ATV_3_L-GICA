ok = False

def prova(a, b, c):
    if divide(a, b) and divide(b, c):
        global ok
        ok = True
        return ok and (f'Se a divide b (a|b), então existe um inteiro k₁ tal que b = a * k₁.\n'
                f'Se b divide c (b|c), então existe um inteiro k₂ tal que c = b * k₂.\n'
                f'Substituindo b = a * k₁ em c = b * k₂, temos c = (a * k₁) * k₂ = a * (k₁ * k₂).\n'
                f'Portanto, como c = a * (k₁ * k₂), podemos concluir que a divide c (a|c).\n')
    else:
        return 'A condição não é válida porque a não divide b ou b não divide c.'

def divide(x, y):
    # Verifica se x divide y
    return y % x == 0

# Testando com os valores de a, b e c
a = 3
b = 9
c = 27


print(prova(a, b, c))
print("exemplo: ")

if ok == True:
    print(f"A divide B = {b} / {a} = {b/a}\n"
          f"B divide C = {c} / {b} = {c/b}\n"
          f"logo:\nA divide C = {c} / {a} = {c/a}")

else:
    print("A condição não foi satisfeita, então não é possível realizar a divisão.")
