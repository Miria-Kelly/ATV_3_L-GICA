def prova(k):

    if impar(k) ==  'impar':
        return (f'Se x² = 2k₁ + 1, então x = 2k₂ + 1.\n'
                f'Vamos proceder por contradição, assumindo que x é par e verificar o que acontece.\n'
                f'Se x é par, então (2x)² = 4x².\n'
                f'Observe que 4x² é par, pois é múltiplo de 2.\n'
                f'Dessa forma, o quadrado de um número par sempre será par.\n'
                f'Portanto, se o quadrado de x é ímpar, x não pode ser par, logo x deve ser ímpar.\n')
    else:
        return "O número é par, então a prova não se aplica."

def impar(k):
    if k % 2 != 0:
        return 'impar'
    else:
        return 'par'

def quadrado(k):
    eh_impar = impar(k)
    if eh_impar == 'impar':
        quadrado = k ** 2
        quadrado_eh_impar = impar(quadrado)
        if quadrado_eh_impar == 'impar':
            return f'O número {k} é ímpar e seu quadrado é {quadrado}, que também é ímpar.'
        else:
            return f'Houve um erro: o número {k} é ímpar, porém o quadrado de {k} é {quadrado}, que é par.'
    else:
        quadrado = k ** 2
        return f'O número {k} é par, e seu quadrado é {quadrado}, que é par.'

# testando com o valor de k

k = 3

print(prova(k))
print("Exemplo: ")
print(quadrado(k))
