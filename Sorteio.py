def sorteia_questao_inedita(questoes, nivel, questoes_sorteadas):
    questoes_nivel = [questao for questao in questoes if questao['nivel'] == nivel and questao not in questoes_sorteadas]

    if questoes_nivel:
        questao_sorteada = random.choice(questoes_nivel)
        questoes_sorteadas.append(questao_sorteada)
        return questao_sorteada
    else:
        print(f"Não há mais perguntas inéditas disponíveis para o nível {nivel}.")
        return None

def questao_para_texto(questao, id):
    texto = f"----------------------------------------\nQUESTAO {id}\n\n{questao['titulo']}\n\nRESPOSTAS:\n"
    for opcao, resposta in questao['opcoes'].items():
        texto += f"{opcao}: {resposta}\n"
    return texto