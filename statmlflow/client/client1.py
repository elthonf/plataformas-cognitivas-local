
import requests
import pandas as pd


if __name__ == "__main__":
    # Carrega os dados
    mydf = pd.read_csv('../../datasets/BaseUnknown03.csv')

    mysample = mydf.sample(20).drop('nome', axis=1)

    # Prepara chamada
    url = "http://127.0.0.1:1234/invocations" #Coloque aqui a porta escolhida
    headers = {'Content-Type': 'application/json'}
    conteudo = mysample.to_json( orient='split')

    #Chama API
    response = requests.request("POST", url, headers=headers, data=conteudo)
    print("Resposta da API:")
    print(response.text.encode('utf8').decode())
    pass

