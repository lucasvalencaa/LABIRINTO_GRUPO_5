from time import sleep

PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "2"
ROBO = "4"
SAIDA = "S"

ESQUERDA = [0, -1]
DIREITA  = [0, 1]
CIMA     = [-1, 0]
BAIXO    = [1, 0]

LABIRINTO = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], 
    ['#', '#', '#', '#', '#', '#', ' ', ' ', '4', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], 
    ['#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], 
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], 
    ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#'], 
    ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'], 
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'S', '#']
]


def print_labirinto():
    print("")
    for linha in LABIRINTO:
        print("".join(linha))
    print("")


def movimento(posicao: tuple, direcao: list):
    LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
    LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
    return [posicao[0] + direcao[0], posicao[1] + direcao[1]]
    

def verifica_movimento(posicao: tuple, direcao: list) -> bool:        
    return (LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == CAMINHO_LIVRE) or (LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == SAIDA)  


def main():

    POSICAO_INICIAL = [3, 8]

    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO

    print_labirinto()

    LISTA_PERCORRIDO = [[3, 8]]

    POSICAO_SAIDA = [9, 18]

    POSICAO_ATUAL = POSICAO_INICIAL

    while POSICAO_ATUAL != POSICAO_SAIDA:
        
        if verifica_movimento(POSICAO_ATUAL, BAIXO):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
            LISTA_PERCORRIDO.append(POSICAO_ATUAL)
            print_labirinto()
            sleep(1)

        elif verifica_movimento(POSICAO_ATUAL, ESQUERDA):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, ESQUERDA)
            LISTA_PERCORRIDO.append(POSICAO_ATUAL)
            print_labirinto()
            sleep(1)

        elif verifica_movimento(POSICAO_ATUAL, CIMA):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, CIMA)
            LISTA_PERCORRIDO.append(POSICAO_ATUAL)
            print_labirinto()
            sleep(1)
        
        elif verifica_movimento(POSICAO_ATUAL, DIREITA):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
            LISTA_PERCORRIDO.append(POSICAO_ATUAL)
            print_labirinto()
            sleep(1)
        
        else:
            ULTIMA_POSICAO = LISTA_PERCORRIDO.pop()
            LABIRINTO[ULTIMA_POSICAO[0]][ULTIMA_POSICAO[1]] = CAMINHO_PERCORRIDO    
            POSICAO_ATUAL = (LISTA_PERCORRIDO[-1])
            LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = ROBO
            print_labirinto()
            sleep(1)

    print ("Sucesso! Você chegou à saída!")     
    
if __name__ == "__main__":
    main()