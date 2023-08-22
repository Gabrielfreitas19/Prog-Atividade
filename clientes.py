# cadastro e exibição de clientes
listclientes:[]
while True:
    nome= input ("digite o nome do client:")
    if nome.lower=="sair":
        print("vc esta saindo...")
        break
    else:
         listclientes.append(nome.capitalize)
         
         listclientes.sort()
    
    for client in listclientes:
            print(client)
    
