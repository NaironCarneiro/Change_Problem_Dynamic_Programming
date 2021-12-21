
def retornaMenores(vet, val):
    vet.sort(reverse=True)
    guardarMenor = []
    for i in range(len(vet)):
        if (vet[i] <= val):
            guardarMenor.append(vet[i])
    return guardarMenor
    
def calculaMoedas(v, val):
    correct = True
    cont = 1
    a = True
    usadas = []
    v = retornaMenores(v,val)
    for y in range(len(v)):
        res = v[y] * 2
        if (res == val):
            print("Troco passado com sucesso")
            print('Foi usada a moeda', v[y], ', com um total de', 2, 'vezes')
            correct = False
            break

    if(correct):
        for x in range(len(v)):

            if (v[0] == val):
                print("Troco passado com sucesso")
                print('Foi usada a moeda',v[0], ', com um total de', cont, 'vez')
                break
            else:
                if(v[x] < val):
                    usadas.append(v[x])
                    val = val - v[x]
                    cont += 1
                    if (v[x] == val and a):
                        print("Troco passado com sucesso")
                        print('Foi usada a moeda', usadas, ', ela foi usada', cont, 'vezes!')
                        # if (v[x] == val and a and v[x] == ):
                        #     print("Troco passado com sucesso")
                        #     print('Foi usada a moeda', usadas, ', ela foi usada', cont, 'vezes!')
                        break


                else:
                    if (a):
                        a = False
                        usadas.append(v[x])
                        print("Troco passado com sucesso")
                        print('Foi usada as moeda', usadas, ', ou seja', cont, 'moedas')



print('Qual o valor do troco do cliente: ')
valor = float(input())

# valores = [5, 10, 25, 50, 100]
valores = [1, 2, 8, 14, 25]
calculaMoedas(valores,valor)