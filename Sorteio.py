import random

def sorteia_questao(dicionario_questoes, nivel):
    questoes_nivel = dicionario_questoes.get(nivel, [])
    if questoes_nivel:
        return random.choice(questoes_nivel)
    else:
        return None
def sorteia_questao_inedita(questoes, nivel, questoes_sorteadas):
    questoes_nivel = questoes[nivel]
    random.shuffle(questoes_nivel)
    
    for questao in questoes_nivel:
        if questao not in questoes_sorteadas:
            questoes_sorteadas.append(questao)
            return questao

    return None

def questao_para_texto(questao, id):
    texto = f"----------------------------------------\nQUESTAO {id}\n\n{questao['titulo']}\n\nRESPOSTAS:\n"
    for opcao, resposta in questao['opcoes'].items():
        texto += f"{opcao}: {resposta}\n"
    return texto
