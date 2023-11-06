#Usa o 'for' para somar todos os dígitos de n
def f_num_sorte(n):
    contagem = 0
    for x in str(n):
        contagem += int(x)
    return contagem
        

def main():

    #Entrada de Dados
    while True:
        try:
            d_aniv = int(input())
        except ValueError:
            print("Digite uma data 'ddmmaaaa'")
            continue
        else:
            break
    #Saída de Dados
    if 0 < d_aniv < 100000000 : 
        print(f'{f_num_sorte(d_aniv)}')


if __name__ == '__main__':
    main()
    
