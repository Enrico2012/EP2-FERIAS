import random

def transforma_base(lista_questoes):
    questoes_por_nivel = {}
    for questao in lista_questoes:
        nivel = questao['nivel']
        if nivel not in questoes_por_nivel:
            questoes_por_nivel[nivel] = []
        questoes_por_nivel[nivel].append(questao)
    return questoes_por_nivel

def valida_questao(questao):
    retorno = {}
    chaves_questao = {'titulo', 'nivel', 'opcoes', 'correta'}
    chaves_opcoes = {'A', 'B', 'C', 'D'}
    niveis = {'facil', 'medio', 'dificil'}
    
    for chave in chaves_questao:
        if chave not in questao:
            retorno[chave] = 'nao_encontrado'
            
    if len(questao) != 4:
        retorno['outro'] = 'numero_chaves_invalido'
        
    if 'titulo' in questao and not questao['titulo'].strip():
        retorno['titulo'] = 'vazio'
    
    if 'nivel' in questao and questao['nivel'] not in niveis:
        retorno['nivel'] = 'valor_errado'
        
    if 'opcoes' in questao:
        if len(questao['opcoes']) != 4:
            retorno['opcoes'] = 'tamanho_invalido'
        else:
            opcoes_vazias = {}
            for opcao in chaves_opcoes:
                if opcao not in questao['opcoes']:
                    opcoes_vazias[opcao] = 'chave_invalida_ou_nao_encontrada'
                elif not questao['opcoes'][opcao].strip():
                    opcoes_vazias[opcao] = 'vazia'
            if opcoes_vazias:
                retorno['opcoes'] = opcoes_vazias
    
    if 'correta' in questao and questao['correta'] not in chaves_opcoes:
        retorno['correta'] = 'valor_errado'
    
    return retorno

def valida_questoes(lista_questoes):
    return [valida_questao(questao) for questao in lista_questoes]


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

def gera_ajuda(questao):
    respostas_incorretas = [v for k, v in questao['opcoes'].items() if k != questao['correta']]
    random.shuffle(respostas_incorretas)
    qtd_dicas = random.randint(1, 2)
    dicas = respostas_incorretas[:qtd_dicas]
    return f"DICA:\nOpções certamente erradas: { ' | '.join(dicas) }"

def valida_resposta(resposta):
    while resposta.lower() not in {'a', 'b', 'c', 'd', 'pula', 'ajuda'}:
        print("Resposta inválida. Escolha uma opção válida (A, B, C, D, pula ou ajuda).")
        resposta = input("Escolha uma opção: ")
    return resposta.lower()


