def f_rendimento(a, b):
    #Constantes
    tax_poup = 0.007
    tax_carro = 0.004
    mes = 0

    while a < b:
        a *= (tax_poup + 1)
        b *= (tax_carro + 1)
        mes += 1

    print(mes)


def main():

    #Determina o valor da poupança e do carro
    v_poupanca = 10000.00
    v_carro = float(input())

    #Imprime em quantos meses a poupança renderá
    #dinheiro suficiente
    f_rendimento(v_poupanca, v_carro)

if __name__ == '__main__':
    main()
