import requests
import os
import threading


if __name__ == "__main__":
    print(f"Sou o processo client, id: {os.getpid()}, thread: {threading.current_thread().ident}")
    # Prepara chamada
    valor1 = input("Digite o primeiro valor:")
    valor2 = input("Digite o segundo valor:")
    url = f"http://127.0.0.1:8080/soma?p1={valor1}&p2={valor2}"
    headers = {'Content-Type': 'application/json'}

    #Chama API
    response = requests.request("POST", url, headers=headers)
    print("Resposta da API:")
    print(response.text.encode('utf8').decode())

    pass

