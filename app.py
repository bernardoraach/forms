
# print("--- Sistema de Geração de Formulários")

# nome= input("Digite seu nome: ")
# cpf = input("Digite o seu CPF: ")
# nome_filho = input("Nome do filho: ")
# renda = input("Renda média no valor de: ")

# #testando
# print("\n Dados Recebidos com Sucesso")
# print(f"\n Nome informado: {nome}")
# print(f"\n CPF informado: {cpf}")
# print(f"\n Filho informado: {nome_filho}")
# print(f"\n Renda mensal aproximada de: {renda}")


#dicionários e funções
from typing import final


def gerar_doc(dados, tipo): 
    """Função que centraliza a lógica de qual formulário gerar"""

    if tipo == "1":
        return f"Eu, {dados['nome']}, inscrito no CPF {dados['cpf']}, venho por meio deste apresentar meu pedido de demissão."

    elif tipo == "2":
        return f"DECLARAÇÃO DE RESPONSÁVEIS: Eu, {dados['nome']}, portador do CPF {dados['cpf']}, autorizo meu filho a participar da viagem escolar com destino à Disney"
    
    
    elif tipo == "3":
        return f"DECLARAÇÃO DE RESIDÊNCIA: Eu, {dados['nome']}, portador do CPF {dados['cpf']}, declaro que resido no endereço {dados['endereco']} referente ao trabalho de autônomo de desenvolvedor."

    elif tipo == "4":
        return f"DECLARAÇÃO DE RENDA: Eu, {dados['nome']}, portador do CPF {dados['cpf']}, declaro que recebo o valor médio de {dados['renda']} referente ao trabalho de autônomo de desenvolvedor."

    else:
        return "!Erro: Esse formulário ainda não existe!"

#salvar em arquivo
    # Função do Back-end para criar e escrever em um arquivo físico
    #with open: abre o arquivo. o "w" significa 'write' (escrever/subescrever)
    #'enconding="utf-8", serve para não quebrar os acentos em portugues
def salvar (arquivo, conteudo):

    with open(arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)
        print(f"\nArquivo salvo na pasta '{arquivo}'")
    
# coleta de dados
# criando dicionário pessoa

pessoa = {}

pessoa['nome'] = input("Nome completo: ")
pessoa['cpf'] = input("CPF: ")
pessoa['filho'] = input("Nome do filho (caso não tiver, pressione a tecla enter): ")
pessoa['endereco'] = input("Endereco completo: ")
pessoa['renda'] = input("Renda mensal: ")

# usuário escolhendo formulário
print("\n[1] Demissão | [2] Responsáveis | [3] Residência | [4] Renda")
selecionar= input("Digite o número da opção: ")


# print("\nSelecione o documento que deseja gerar: ")
# print("[1] Pedido de demissão ")
# print("[2] Declaração de Responsáveis")
# print("[4] Declaração de Residência")
# print("[3] Declaração de Renda")


doc_final = gerar_doc(pessoa, selecionar)

print("\n-----------DOCUMENTO GERADO-----------")
print(doc_final)
print("----------------------")

if "Erro: " not in doc_final:
    nome_arquivo = f"documento_{pessoa['nome'].lower().replace(' ', '-')}.txt"

salvar(nome_arquivo, doc_final)