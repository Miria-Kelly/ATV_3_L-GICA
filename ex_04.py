def prova(a, b):
    if eh_par(a) and eh_impar(b) or eh_par(b) and eh_impar(a):
        return (f'Se a = 2k₁ (par) e b = 2k₂ + 1 (ímpar), então a soma de a e b é (2k₁) + (2k₂ + 1).\n'
                f'Isso resulta em 2(k₁ + k₂) + 1, que é da forma 2n + 1, ou seja, um número ímpar.\n'
                f'Portanto, a soma de um número par com um número ímpar sempre será ímpar.\n')
    else:
        return 'A prova não se aplica porque um dos números não é par ou ímpar como esperado.'

def eh_par(n):
    return n % 2 == 0

def eh_impar(n):
    return n % 2 != 0

def soma_par_impar(a, b):
    if eh_par(a) and eh_impar(b) or eh_par(b) and eh_impar(a):
        soma = a + b
        if eh_impar(soma):
            return f'A soma de {a} (par) e {b} (ímpar) é {soma}, que é um número ímpar.'
        else:
            return f'Houve um erro: a soma de {a} e {b} deveria ser ímpar, mas resultou em um número par.'
    else:
        return 'Um ou ambos os números não estão nas categorias corretas de par ou ímpar.'

# Testando com valores de a (par) e b (ímpar)
a = 2
b = 5

print(prova(a, b))
print("Exemplo:")
print(soma_par_impar(a, b))
