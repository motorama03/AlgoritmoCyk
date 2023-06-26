def parse(gramatica, cadeia):
    n = len(cadeia)
    r = len(gramatica)
    P = [[set() for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for regra in gramatica:
            for producao in gramatica[regra]:
                if cadeia[i] == producao:
                    P[i][i].add(regra)
    
    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            for k in range(i, j):
                for regra in gramatica:
                    for producao in gramatica[regra]:
                            if len(producao) == 2:
                                B, C = producao
                            if B in P[i][k] and C in P[k + 1][j]:
                                P[i][j].add(regra)
    
    return "S" in P[0][n - 1]

# Gramática para a resolução da atividade proposta:
gramatica = {
    "S": ["AB", "XB", "XS"], # "XS" foi criado para a implementação da matriz feita no caderno ;)
    "A": ["a"],
    "B": ["b"],
    "X": ["AS"]
}

cadeia = input("Digite uma cadeia: ")

pertence = parse(gramatica, cadeia)
print("Linguagem aceita!" if pertence else "Linguagem não aceita!")
