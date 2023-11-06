#Utiliza um loop com 'while' para calcular
#em quanto tempo a lebre alcançará a tartaruga
def f_corrida(v1, v2):
    tempo = 0
    while v1 > v2:
        v1 += 1
        v2 += 10
        tempo += 1
    print(tempo)
        


def main():

    #Digita a vantagem da tartarguga
    vantagem  = int(input())
    pos_lebre = 0

    #Mostra na tela o tempo para que a lebre
    #alcance a tartaruga
    f_corrida(vantagem, pos_lebre)


if __name__ == '__main__':
    main() 

    
