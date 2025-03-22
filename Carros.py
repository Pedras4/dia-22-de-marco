marca = input("Qual a marca de carro que deseja consultar?")

if marca in "Ford Chevrolet Dodge":
    print(marca,"é americana")
elif marca in "Honda Toyota Suzuki Nissan":
    print(marca, "é asiática")
elif marca in "Peugeot Cintroen BMW":
    print(marca, "é europeia")
else:
    print ("Desculpa!",marca,"não está em nossa base de dados")