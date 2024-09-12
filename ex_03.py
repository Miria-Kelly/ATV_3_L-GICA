def prova(a, b):
    if eh_par(a) and eh_par(b):
        return (f'Se a = 2k₁ e b = 2k₂, então a soma de a e b é dada por (2k₁) + (2k₂).\n'
                f'Isso resulta em 2(k₁ + k₂), que é claramente divisível por 2, logo é um número par.\n'
                f'Portanto, a soma de dois números pares sempre será par.\n')
    else:
        return 'A prova não se aplica porque um ou ambos os números não são pares.'

def eh_par(n):
    return n % 2 == 0

def soma_pares(a, b):
    if eh_par(a) and eh_par(b):
        soma = a + b
        if eh_par(soma):
            return f'A soma de {a} e {b} é {soma}, que é um número par.'
        else:
            return f'Houve um erro: a soma de {a} e {b} deveria ser par, mas resultou em um número ímpar.'
    else:
        return 'Um ou ambos os números não são pares.'

# Testando com valores de a e b
a = 8
b = 2

print(prova(a, b))
print("Exemplo:")
print(soma_pares(a, b))
