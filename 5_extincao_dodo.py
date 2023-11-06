#Calcula a população total
def f_populacao(a, b):
    nasc = a * 0.01
    mortes = a * 0.06
    total = (a * 0.94) + (a * 0.01)

    while True:
        #Imprime os anos, nascimento, mortes e populaçao final
        print(f'{b},{nasc:.0f},{mortes:.0f},{total:.0f}')
        b += 1
        nasc = total * 0.01
        mortes = total * 0.06
        total = (total * 0.94) + nasc 
        if total < a * 0.10:
            print(f'{b},{nasc:.0f},{mortes:.0f},{total:.0f}')
            break

        
def main():
    #Entrada de Dados
    pop_dodo = int(input())
    ano = 1600

    #Saída de Dados
    f_populacao(pop_dodo, ano)
    

if __name__ == '__main__':
    main()
