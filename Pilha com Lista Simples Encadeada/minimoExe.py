# Ajuste os métodos abaixo psuh_aux, pop_aux e get_min para que # seja possível
# encontrar o elemento mínimo de uma pilha simplesmente buscando no topo (peek) da pilha min_stack.

from stack import Stack

if __name__ == "__main__":
    main_stack = Stack()
    min_stack = Stack()

    def push_aux(data):
        """
        Função para empilhar na pilha principal e atualizar a pilha de mínimos quando necessário.
        """
        main_stack.push(data)
        if min_stack.is_empty() or data <= min_stack.peek(): #peek: apenas olha o valor que está no topo da pilha
            min_stack.push(data) #se o número é menor ou igual ao valor atual no topo da pilha de mínimos, ele entra na pilha min_stack()."


    def pop_aux():
        """
        Função para desempilhar da pilha principal e atualizar a pilha de mínimos quando necessário.
        """
        topo = main_stack.pop() #remove o último valor da pilha principal
        if topo == min_stack.peek(): #verifica se o valor removido da pilha principal é igual ao topo da pilha de mínimos
            min_stack.pop() #se for igual, remove esse valor
            

    def get_min():
        """
        Função para retornar o mínimo atual.
        """
        minimo_atual = min_stack.peek()
        return minimo_atual

    # Testes
    print("\nEmpilhando: 5, 3, 7, 2, 8")
    push_aux(5)
    print(f"Min atual: {get_min()}")

    push_aux(3)
    print(f"Min atual: {get_min()}")

    push_aux(7)
    print(f"Min atual: {get_min()}")

    push_aux(2)
    print(f"Min atual: {get_min()}")

    push_aux(8)
    print(f"Min atual: {get_min()}")

    print("\nDesempilhando e mostrando o mínimo:")
    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    try:
        print(get_min())
    except IndexError as e:
        print(f"Erro esperado: {e}")
