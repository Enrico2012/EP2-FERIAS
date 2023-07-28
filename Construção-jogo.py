import random
from colorama import Fore, Style

questoes = [
    {"titulo": "Qual é a capital do Brasil?", "nivel": "facil", "opcoes": {"A": "Rio de Janeiro", "B": "Brasília", "C": "São Paulo", "D": "Belo Horizonte"}, "correta": "B"},
    {"titulo": "Qual é a moeda do Japão?", "nivel": "facil", "opcoes": {"A": "Dólar", "B": "Yuan", "C": "Euro", "D": "Iene"}, "correta": "D"},
    {"titulo": "Quem escreveu 'Dom Casmurro'?", "nivel": "medio", "opcoes": {"A": "Machado de Assis", "B": "Aluísio Azevedo", "C": "José de Alencar", "D": "Jorge Amado"}, "correta": "A"},
    {"titulo": "Em que ano aconteceu o golpe militar no Brasil?", "nivel": "medio", "opcoes": {"A": "1960", "B": "1962", "C": "1964", "D": "1966"}, "correta": "C"},
    {"titulo": "Qual é o maior planeta do sistema solar?", "nivel": "dificil", "opcoes": {"A": "Marte", "B": "Vênus", "C": "Júpiter", "D": "Saturno"}, "correta": "C"},
    {"titulo": "Qual é a fórmula química da água?", "nivel": "dificil", "opcoes": {"A": "H2O", "B": "CO2", "C": "NaCl", "D": "O2"}, "correta": "A"},
    {"titulo": "Qual é a capital da Espanha?", "nivel": "facil", "opcoes": {"A": "Barcelona", "B": "Valência", "C": "Madrid", "D": "Sevilha"}, "correta": "C"},
    {"titulo": "Quem pintou a Mona Lisa?", "nivel": "medio", "opcoes": {"A": "Leonardo da Vinci", "B": "Pablo Picasso", "C": "Vincent van Gogh", "D": "Michelangelo"}, "correta": "A"},
    {"titulo": "Qual é o maior animal terrestre?", "nivel": "dificil", "opcoes": {"A": "Elefante Africano", "B": "Girafa", "C": "Baleia Azul", "D": "Rinoceronte-branco"}, "correta": "A"},
    {"titulo": "Quantos elementos químicos a tabela periódica possui?", "nivel": "dificil", "opcoes": {"A": "118", "B": "90", "C": "63", "D": "105"}, "correta": "A"},
    {"titulo": "Qual é o rio mais longo do mundo?", "nivel": "medio", "opcoes": {"A": "Rio Nilo", "B": "Rio Amazonas", "C": "Rio Amarelo", "D": "Rio Ganges"}, "correta": "B"},
    {"titulo": "Em que país nasceu o famoso compositor Johann Sebastian Bach?", "nivel": "medio", "opcoes": {"A": "Áustria", "B": "Alemanha", "C": "Itália", "D": "França"}, "correta": "B"},
    {"titulo": "Qual é o símbolo químico do oxigênio?", "nivel": "facil", "opcoes": {"A": "O", "B": "Xe", "C": "Co", "D": "Ne"}, "correta": "A"},
    {"titulo": "Quem foi o primeiro presidente do Brasil?", "nivel": "medio", "opcoes": {"A": "Getúlio Vargas", "B": "José Sarney", "C": "Juscelino Kubitschek", "D": "Deodoro da Fonseca"}, "correta": "D"},
    {"titulo": "Qual é o maior deserto do mundo?", "nivel": "medio", "opcoes": {"A": "Saara", "B": "Gobi", "C": "Atacama", "D": "Carcóvia"}, "correta": "A"},
    {"titulo": "Qual é o livro mais vendido da história, excluindo-se livros religiosos?", "nivel": "dificil", "opcoes": {"A": "Dom Quixote", "B": "Harry Potter e a Pedra Filosofal", "C": "O Pequeno Príncipe", "D": "Cem Anos de Solidão"}, "correta": "A"},
    {"titulo": "Qual é a capital da Rússia?", "nivel": "facil", "opcoes": {"A": "São Petersburgo", "B": "Moscovo", "C": "Kazan", "D": "Sochi"}, "correta": "B"},
    {"titulo": "Em qual país foi sediada a primeira Copa do Mundo de futebol?", "nivel": "medio", "opcoes": {"A": "Brasil", "B": "Argentina", "C": "Uruguai", "D": "França"}, "correta": "C"},
    {"titulo": "Quem foi o pintor das obras 'Guernica' e 'Les Demoiselles d'Avignon'?", "nivel": "medio", "opcoes": {"A": "Pablo Picasso", "B": "Salvador Dalí", "C": "Claude Monet", "D": "Vincent van Gogh"}, "correta": "A"},
    {"titulo": "Qual é o maior animal marinho?", "nivel": "dificil", "opcoes": {"A": "Baleia-azul", "B": "Tubarão-branco", "C": "Polvo-gigante", "D": "Orca"}, "correta": "A"},
]

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


def introducao():
    print(Fore.YELLOW + "Bem-vindo ao jogo da fortuna! Aqui é onde você pode testar seu conhecimento e ganhar prêmios!\n"
          "Cada rodada apresenta uma pergunta de múltipla escolha. Se você responder corretamente, ganha dinheiro.\n"
          "A quantidade de dinheiro aumenta a cada rodada, mas cuidado! Se você responder incorretamente, você perde tudo.\n"
          "Você também tem a opção de pular ou pedir ajuda se não souber uma resposta.\n"
          "Se você chegar a 1 milhão, você vence o jogo!\n"
          "Vamos começar! Boa sorte!" + Style.RESET_ALL)

def mensagem_vitoria(nome_jogador):
    print(Fore.GREEN + f"Parabéns, {nome_jogador}! Você alcançou 1 milhão! Você é o grande vencedor do jogo da fortuna!" + Style.RESET_ALL)

def jogo_fortuna(nome_jogador, questoes, premios):
    niveis = ["facil", "medio", "dificil"]
    while True:  
        introducao()
        questoes_sorteadas = []
        premio_atual = 0
        for idx, premio in enumerate(premios):  
            if idx < len(premios) // 3:
                nivel = niveis[0]
            elif idx < 2 * len(premios) // 3:
                nivel = niveis[1]
            else:
                nivel = niveis[2]
            
            questao = sorteia_questao_inedita(questoes, nivel, questoes_sorteadas)
            if questao is None:
                break

            questoes_sorteadas.append(questao)
            print(questao_para_texto(questao, premio))
            resposta = valida_resposta(input("Escolha uma opção: "))

            if resposta == "pula":
                print("Você escolheu pular essa pergunta.")
                continue

            if resposta == "ajuda":
                print(gera_ajuda(questao))
                resposta = valida_resposta(input("Escolha uma opção: "))

            if resposta == questao['correta'].lower():
                print(Fore.GREEN + "Resposta correta!" + Style.RESET_ALL)
                premio_atual = premio
                print(f"Você agora tem {premio_atual}.")
                if premio_atual == 1000000:
                    mensagem_vitoria(nome_jogador)
                    break
                if input("Você quer continuar jogando? (S/N): ").lower() != 's':
                    break
            else:
                print(Fore.RED + "Resposta errada. Você perdeu tudo!" + Style.RESET_ALL)
                premio_atual = 0
                break

        print(Fore.BLUE + f"Obrigado por jogar, {nome_jogador}! Você ganhou {premio_atual}." + Style.RESET_ALL)

        if input("Deseja jogar novamente? (S/N): ").lower() != 's':
            break  
nome = input("Informe seu nome: ")
jogo_fortuna(nome, questoes, [1000, 5000, 10000, 50000, 100000, 500000, 1000000])
