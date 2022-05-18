# monta um grafo a partir de um conjunto de valores com regras definidas
# line_a deve possuir o mesmo tamanho de line_b, cujo valor deve ser passado na variavel leng
# start_p sao os valores o qual serao o custo para entrar na linha a ou b do grafo (neste tipo de grafo temos que o ponto 0 esta a esquerda do valor retornado e tem peso 0 absoluto)
# finish_p sao os valores para sair do grafo em a e b (assim chegando no final cujo valor nao pertence a line a ou b tem valor absoluto 0)
# retorna uma lista do tipo: list[list[list[int]]], cujo list[int] pode ser descrito como (a, v), sendo a o valor da aresta e v o da vertice, sua list anterior mantem as linhas e a superior une tudo em um grafo
def get_grafo(line_a: list[int] or list[float], line_b: list[int] or list[float], start_p: list[int] or list[float], finish_p: list[int] or list[float], switch_a: list[int] or list[float], switch_b: list[int] or list[float], leng: int) -> list:
    grafo = list()
    grafo.append([[start_p[0], line_a[0]]])
    grafo.append([[start_p[1], line_b[0]]])
    for i in range(1, leng):
        j = i - 1
        grafo[0].append([switch_a[j], line_a[i]])
        grafo[1].append([switch_b[j], line_b[i]])
    grafo[0].append([finish_p[0], 0])
    grafo[1].append([finish_p[1], 0])
    return grafo
# funcao ainda sera generalizada
