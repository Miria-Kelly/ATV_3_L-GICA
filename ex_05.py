def prova(a, b):
    if eh_impar(a) and eh_impar(b):
        return (f'Se a = 2k₁ + 1 e b = 2k₂ + 1, então o produto de a e b é (2k₁ + 1) * (2k₂ + 1).\n'
                f'Isso resulta em (2k₁ * 2k₂ + 2k₁ + 2k₂ + 1), que pode ser reescrito como 2(k₁ * 2k₂ + k₁ + k₂) + 1.\n'
                f'Esse resultado é da forma 2n + 1, ou seja, um número ímpar.\n'
                f'Portanto, o produto de dois números ímpares sempre será ímpar.\n')
    else:
        return 'A prova não se aplica porque um ou ambos os números não são ímpares.'

def eh_impar(n):
    return n % 2 != 0

def produto_impares(a, b):
    if eh_impar(a) and eh_impar(b):
        produto = a * b
        if eh_impar(produto):
            return f'O produto de {a} e {b} é {produto}, que é um número ímpar.'
        else:
            return f'Houve um erro: o produto de {a} e {b} deveria ser ímpar, mas resultou em um número par.'
    else:
        return 'Um ou ambos os números não são ímpares.'

# Testando com valores de a e b
a = 3
b = 5

print(prova(a, b))
print("Exemplo:")
print(produto_impares(a, b))
