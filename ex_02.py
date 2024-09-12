def prova(a, b):
    if eh_par(a) and eh_par(b):
        return (f'Se a = 2k₁ e b = 2k₂, então o produto de a e b é dado por (2k₁) * (2k₂).\n'
                f'Isso resulta em 4k₁k₂, que é claramente divisível por 2, logo é um número par.\n'
                f'Portanto, o produto de dois números pares sempre será par.\n')
    else:
        return 'A prova não se aplica porque um ou ambos os números não são pares.'

def eh_par(n):
    return n % 2 == 0

def produto_pares(a, b):
    if eh_par(a) and eh_par(b):
        produto = a * b
        if eh_par(produto):
            return f'O produto de {a} e {b} é {produto}, que é um número par.'
        else:
            return f'Houve um erro: o produto de {a} e {b} deveria ser par, mas resultou em um número ímpar.'
    else:
        return 'Um ou ambos os números não são pares.'

# Testando com valores de a e b
a = 4
b = 2

print(prova(a, b))
print("Exemplo:")
print(produto_pares(a, b))
