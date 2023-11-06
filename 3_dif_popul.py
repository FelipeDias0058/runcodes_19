#Calcula o aumento da população a cada ano
def f_dif_popul(a, b):
    #Funções auxiliares
    aux1 = a
    aux2 = b

    #Se a população 'A' for menor, inverte os valores
    if aux1 < aux2:
        a, b = b, a
    
    #Contador de anos
    anos = 0
    while a > b:
        a *= (1 + 0.02)
        b *= (1 + 0.03)
        anos += 1
    print(anos)

def main():
    #Entrada de Dados
    pop_a =  int(input())
    pop_b =  int(input())

    #Saída de Dados
    f_dif_popul(pop_a, pop_b)


if __name__ == '__main__':
    main()
