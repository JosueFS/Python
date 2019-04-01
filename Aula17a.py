# num = [0, 5, 9, 1]
# num[2] = 3 #Atribui na posição 2 o valor 3
# num.append(7) #Adiciona o elemento 7 na ultima posição
# num.insert(2, 9) #Insere o elemento zero na posição 2
# num.sort(reverse=True) #Ordena inversamente
# num.pop() #Remove o ultimo elemento qualquer que seja ele
# if 2 in num:
#     num.remove(2) #Remove o primeiro elemento com o valor 2
# else:
#     print(f'Não achei o número 2.')
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')
# ###############################################################
# valores = []
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
#
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}...!')
# print(f'Fim da lista.')
########################################################
a = [2, 3, 4, 7]
b = a       #Cria uma ligação entre as listas
c = a[:]    #Copia os elementos contidos em uma lista
b[2] = 8
c[2] = 0
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
