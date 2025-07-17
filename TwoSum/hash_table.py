def two_sum(numeros, alvo):
    indice_por_valor = {}  

    for i, valor_atual in enumerate(numeros):
        complemento = alvo - valor_atual

        if complemento in indice_por_valor:
            return [indice_por_valor[complemento], i]
        
        indice_por_valor[valor_atual] = i
    
    return []

if __name__ == "__main__":
    numeros1 = [2, 7, 11, 15]
    alvo1 = 9
    resultado1 = two_sum(numeros1, alvo1)
    print(f"Números: {numeros1}, Alvo: {alvo1} -> Resultado: {resultado1}")

    numeros2 = [3, 2, 4]
    alvo2 = 6
    resultado2 = two_sum(numeros2, alvo2)
    print(f"Números: {numeros2}, Alvo: {alvo2} -> Resultado: {resultado2}")

    numeros3 = [3, 3]
    alvo3 = 6
    resultado3 = two_sum(numeros3, alvo3)
    print(f"Números: {numeros3}, Alvo: {alvo3} -> Resultado: {resultado3}")

    numeros4 = [1, 5, 9, 3]
    alvo4 = 8
    resultado4 = two_sum(numeros4, alvo4)
    print(f"Números: {numeros4}, Alvo: {alvo4} -> Resultado: {resultado4}")