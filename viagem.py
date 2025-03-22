distancia = float(input("Qual foi a distancia da viagem"))
meio_transporte = (input("Qual foi a escolha do meio de transporte"))
preço_por_km = float(input("Qual foi o preço por kilometro do meio de transporte escolhido"))
quantidade_de_pessoas = float(input("quantas pessoas tinha na viagem"))

total = (distancia / preço_por_km)
print ("O preço total foi" , total)
