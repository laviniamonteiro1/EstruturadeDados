# Dado uma string de expressão x. 
# Verifique se os pares e a ordem de ‘{’ , ‘}’ , ‘(’ , ‘)’ , ‘[’ , ‘]’ estão corretos.
# Por exemplo, a função deve retornar:
# ‘True’ para exp = “[()]{}{()()}” e 
# ‘False’ para exp = “[(])”.

from stack import Stack

def is_balanced(expression):
    pilha = Stack()
    pares = {')': '(', ']': '[', '}': '{'} 

    for caractere in expression:
        if caractere in '([{':
            pilha.push(caractere) #adiciona um item no topo pilha(se for caracter de abertura, adiciona no topo)
        elif caractere in ')]}':
            if pilha.is_empty(): #verifica se a pilha está vazia
                return False
            topo = pilha.pop() #remove o caracter que está no topo da pilha(desempilha)
            if topo != pares[caractere]: #compara o caracter que foi desempilhado com o topo atual da pilha
                return False 
        #se os caracteres forem iguais, retorna True
        #se os caracteres forem diferentes retorna False

    return pilha.is_empty()

# Testes
print(is_balanced("[{}(2+2)]{}"))    # Esperado: True
print(is_balanced("[{}(2+2))]{}"))   # Esperado: False
print(is_balanced("[{}])"))          # Esperado: False

