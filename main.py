import requests # Libs
import json 



def consumindo():# Função responsavél pelo processamento do consumo da API

    try:# Inicia bloco de codigo

        # Url da API dos correios
        cepdousuaio = int(input("Por favor informe o seu cep: "))

        url = ('http://viacep.com.br/ws/{}/json/'.format(cepdousuaio))
        
        consindoapi = requests.get(url)# Obitendo os dados 
        consindoapi = consindoapi.json()# Passando os dados para um json

        cep = consindoapi["cep"]# Pegando o cep
        longradouro = consindoapi["logradouro"]# pegando o longradouro
        complemento = consindoapi["complemento"]# pegando o complemento
        bairro = consindoapi["bairro"]
        local = consindoapi["localidade"]
        uf = consindoapi["uf"]
        ibje = consindoapi["ibge"]
        ddd = consindoapi["ddd"]

        print('#'*50)
        print(" Esse é o seu cep: "+cep,'\n',
            "Esse é o seu longradouro: "+longradouro,
            '\n',"Esse é o complemento:"+complemento,
            '\n',"Esse é o bairro: "+bairro,'\n',
            "Esse é a localidade: "+local
            )
        print('#'*50)
        continuar = int(input(" Deseja fazer outra consulta?\n Digite 1 para Sim e 2 para Não"))
        if continuar == 1:
            consumindo()

        elif continuar == 2:
            print('Muito obrigado por usar a nossa API')

        elif not continuar:
            return False
        else:
            print("Fim do programa")
    except Exception as erro:
        print(erro)# Finalizando o bloco de codigo


consumindo()# chamando a função consumindo



