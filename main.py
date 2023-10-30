import os 
os.system ('clear')

idade = int(input("Digite sua idade: \n"))
total = float(input("Digite o valor total dos produtos: \n"))

if(idade>=18):
    print("Pode ter o desconto,")
    desconto = total * 0.1
    final = total - desconto
    print(f"o desconto é de R${desconto:.2f} e o total é de R${final}.")
else:
    print(f"Não tem direito ao desconto e o valor final é R${total}")