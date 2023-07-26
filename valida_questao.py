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