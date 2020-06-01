import requests
import pandas as pd



if __name__ == "__main__":
    # Carrega os dados
    mydf = pd.read_csv('../../datasets/BaseUnknown03.csv')

    # Filtra alguns para testes:
    filtrados = mydf.sample(4)

    # Prepara chamada
    url = "http://localhost:8080/modelo01"
    headers = {'Content-Type': 'application/json'}
    conteudo = filtrados.to_json()

    #Chama API
    response = requests.request("POST", url, headers=headers, data=conteudo)
    print("Resposta da API:")
    print(response.text.encode('utf8').decode())
    pass

