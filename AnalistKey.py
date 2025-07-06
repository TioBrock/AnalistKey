# Cores
R = '\033[91m'  # vermelho
V = '\033[92m'  # verde
A = '\033[93m'  # amarelo
Z = '\033[94m'  # azul
C = '\033[96m'  # ciano
X = '\033[0m'   # resetar


def verificar(senha):
    """
    Avalia a segurança da senha e retorna uma pontuação com dicas.

    :param senha: (str) Senha digitada pelo usuário.
    :return: (tuple) (ponto (int), dicas (list[str])).
    """
    from re import search, compile, VERBOSE

    ponto = 0  # pontuação da senha
    padrao_fraco = r'''  # regex que identifica padrões comuns
    ^(
        [a-zA-Z]{3,}$
        |
        [a-zA-Z]{2,}\d{2,4}$
        |
        [a-zA-Z]{2,}[!"#$%&'()*+,\-./:;<=>?@[\]\\^_`{|}~]$
        |
        [a-zA-Z]{2,}\d{2,4}[!"#$%&'()*+,\-./:;<=>?@[\]\\^_`{|}~]$
        |
        [a-zA-Z]{2,}[!"#$%&'()*+,\-./:;<=>?@[\]\\^_`{|}~]\d{2,4}$
    )
    '''

    dicas = []

    # verificações de composição da senha
    if len(senha) >= 8:
        ponto += 1
    else:
        dicas.append('Sua senha deve haver 8 caracteres ou mais.')

    if search(r'[A-Z]', senha):
        ponto += 1
    else:
        dicas.append('Sua senha deve conter pelo menos 1 maiúscula.')

    if search(r'[a-z]', senha):
        ponto += 1
    else:
        dicas.append('Sua senha deve possuir pelo menos 1 minúscula.')

    if search(r'\d', senha):
        ponto += 1
    else:
        dicas.append('Sua senha deve incluir números.')

    if search(r'''[!"#$%&'()*+,\-./:;<=>?@[\]\\^_`{|}~]''', senha):
        ponto += 1
    else:
        dicas.append('Sua senha deve ter pelo menos um caractere especial.')

    padrao_compilado = compile(padrao_fraco, flags=VERBOSE)

    # detecta padrões comuns usados em senhas
    if padrao_compilado.fullmatch(senha):
        dicas.append('Sua senha segue um padrão comum.')
    else:
        ponto += 1

    return ponto, dicas


def nota(ponto):
    """
    Retorna uma frase de avaliação com base nos pontos.

    :param ponto: (int) Pontuação da senha.
    :return: (str) Mensagem de avaliação.
    """
    if ponto == 6:
        return f'Sua senha é segura! Fez {ponto} pontos.'
    elif ponto >= 4:
        return f'Sua senha é moderada. Fez {ponto} pontos.'
    else:
        return f'Sua senha não é segura. Fez {ponto} pontos.'


def calc_tempo(senha):
    """
    Estima o tempo necessário para quebrar a senha via bruteforce simples.

    :param senha: (str) Senha a ser avaliada.
    :return: (str) Tempo estimado em formato legível.
    """
    from math import log2
    from re import search

    conjunto = 0
    if search(r'[A-Z]', senha):
        conjunto += 26
    if search(r'[a-z]', senha):
        conjunto += 26
    if search(r'\d', senha):
        conjunto += 10
    if search(r'''[!"#$%&'()*+,\-./:;<=>?@[\]\\^_`{|}~]''', senha):
        conjunto += 32

    #  entropia é uma medida do grau de desordem ou aleatoriedade de um sistema
    entropia = log2(conjunto) * len(senha) if conjunto else 0
    tentativas_por_segundo = 1_500_000
    segundos = 2 ** entropia / tentativas_por_segundo
    return formatar_tempo(segundos)


def formatar_tempo(segundos):
    """
    Converte segundos em formato legível (anos, dias, horas...).

    :param segundos: (float) Tempo estimado em segundos.
    :return: (str) Tempo formatado.
    """
    if segundos < 1:
        return 'menos de 1 segundo'
    elif segundos < 60:
        return f'{segundos:,.0f} segundos'.replace(',', '.')
    elif segundos < 3600:
        return f'{segundos / 60:,.0f} minutos'.replace(',', '.')
    elif segundos < 86400:
        return f'{segundos / 3600:,.0f} horas'.replace(',', '.')
    elif segundos < 31_536_000:
        return f'{segundos / 86400:,.0f} dias'.replace(',', '.')
    else:
        return f'{segundos / 31_536_000:,.0f} anos'.replace(',', '.')


def clear():
    """
    Limpa o terminal, em Windows ou Linux.
    """
    from os import system, name
    system('cls' if name == 'nt' else 'clear')


def print_resultados(senha, ponto, dicas):
    """
    Exibe os resultados da análise da senha, com formatação e cores.

    :param senha: (str) Senha analisada.
    :param ponto: (int) Pontuação da senha.
    :param dicas: (list[str]) Sugestões de melhoria.
    """
    print('\n' + '-'*40)
    print(f'Analisando a senha: {V}{senha}{X}')
    print('-'*40)

    avaliacao = nota(ponto)

    # cores de acordo com a nota da senha
    if ponto >= 5:
        print(f'{V}{avaliacao}{X}')
    elif ponto >= 3:
        print(f'{A}{avaliacao}{X}')
    else:
        print(f'{R}{avaliacao}{X}')

    print(
        'Sua senha seria descoberta por um bruteforce simples '
        f'em, aproximadamente: {A}{calc_tempo(senha)}{X}.'
    )

    if dicas:
        print('\nDicas de melhoria:')
        for dica in dicas:
            print(f' - {dica}')


def gerar_senha(tamanho):
    """
    Gera uma senha aleatória com letras, números e símbolos.

    :param tamanho: (int) Tamanho desejado para a senha.
    :return: (str) Senha gerada.
    """
    from random import choice, shuffle

    letras_maius = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letras_minus = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    especiais = r'''!"#$%&'()*+,\./:;<=->?@[]^_`{|}~'''

    senha = [
        choice(letras_maius),
        choice(letras_minus),
        choice(numeros),
        choice(especiais)
    ]

    # preenche o resto da senha com caractere aleatório
    tudo = letras_maius + letras_minus + numeros + especiais
    senha += [choice(tudo) for _ in range(tamanho - 4)]
    shuffle(senha)

    return ''.join(senha)


def menu():
    """
    Menu principal
    """
    while True:
        print(
            '================================\n'
            'SELECIONE UMA DAS OPÇÕES ABAIXO:\n'
            '[1] Verificar Segurança da Senha\n'
            '[2] Gerar Senha Segura\n'
            '[3] Encerrar o programa\n'
        )
        opc = input('Selecione a Opção: ')

        if opc == '1':
            clear()
            senha = input('Digite sua senha: ')
            ponto, dicas = verificar(senha)
            clear()
            print_resultados(senha, ponto, dicas)

        elif opc == '2':
            clear()
            while True:
                try:
                    tamanho = int(input('Digite o tamanho da senha (min 8): '))
                    if tamanho < 8:
                        print('Insira um número maior ou igual a 8.')
                        continue
                    break
                except ValueError:
                    print('Por favor, digite um número válido.')

            senha = gerar_senha(tamanho)
            ponto, dicas = verificar(senha)
            clear()
            print('Avaliação da senha criada:')
            print_resultados(senha, ponto, dicas)

        elif opc == '3':
            clear()
            print('Programa encerrado. Obrigado por usar!')
            break

        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    menu()
