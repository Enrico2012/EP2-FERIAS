import random
def gera_ajuda(questao):
    respostas_incorretas = [v for k, v in questao['opcoes'].items() if k != questao['correta']]
    random.shuffle(respostas_incorretas)
    qtd_dicas = random.randint(1, 2)
    dicas = respostas_incorretas[:qtd_dicas]
    return f"DICA:\nOpções certamente erradas: { ' | '.join(dicas) }"
