from stack import Stack

class FilaComPilhas:
    def __init__(self):
        self.pilha_entrada = Stack()
        self.pilha_saida = Stack()
    
    def enqueue(self, item):
        self.pilha_entrada.push(item)
        print(f"{item} enfileirado com sucesso.")
    
    def dequeue(self):
        if self.pilha_saida.is_empty():
            while not self.pilha_entrada.is_empty():
                elemento = self.pilha_entrada.pop()
                self.pilha_saida.push(elemento)
        if self.pilha_saida.is_empty():
            raise IndexError("Fila vazia: Não é possível remover.")
        
        return self.pilha_saida.pop()
    
    def is_empty(self):
        return self.pilha_entrada.is_empty() and self.pilha_saida.is_empty()
    
    def peek(self):
        if self.pilha_saida.is_empty():
            while not self.pilha_entrada.is_empty():
                self.pilha_saida.push(self.pilha_entrada.pop())
        if self.pilha_saida.is_empty():
            raise IndexError("Fila vazia: Não é possível espiar.")
        
        return self.pilha_saida.peek()
    
    def __str__(self):
        itens = []
        while not self.is_empty():
            itens.append(self.dequeue())
        for item in itens:
            self.enqueue(item)
            
        return " <- ".join(map(str, itens))