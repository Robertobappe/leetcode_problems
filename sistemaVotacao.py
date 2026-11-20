def sistemaVotacao(matriz):
    votos = {}
    L = []

    for voto in matriz:
        for i in range(3):
            if voto[i] not in votos:
                votos[voto[i]] = 0           
            votos[voto[i]] += 3 - i                
    maxVotos =max(votos.values(), default=None)

    if maxVotos is None:
        return []
    for chave, valor in votos.items():
        if valor == maxVotos:
            L.append(chave)
    return L   
            
                
matriz = [["alice", "bob", "carol"],["alice", "bob", "carol"],["bob","carol", "alice"]]
print(sistemaVotacao(matriz))