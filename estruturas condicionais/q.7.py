idade=int(input("digite sua idade: "))
if idade <=12:
    print("voce é criança.")
elif idade >12 and idade <18:
    print("voce é adolecente.")
elif idade >=18 and idade <50:
    print("vc é adulto.")
else:
    print("voce é idoso")