import joblib
import pandas as pd
import json
import numpy as np
from flask import Flask, jsonify, request
import os
import threading

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = NpEncoder

@app.route("/", methods=['GET', 'POST'])
def call_home(request = request):
    print(f"Sou o processo server, id: {os.getpid()}, thread: {threading.current_thread().ident}")
    print(request.values)
    return "SERVER IS RUNNING!"

@app.route("/soma", methods=['GET', 'POST'])
def call_soma(request = request):
    print(f"Sou o processo server, id: {os.getpid()}, thread: {threading.current_thread().ident}")
    print(request.values)

    try:
        p1 = request.values.get('p1')
        if p1 is None:
            raise NotImplementedError("Parametro p1 obrigatório.")
        p2 = request.values.get('p2')

        try:
            par1 = float(p1)
            par2 = float(p2)
        except:
            raise Exception("Os parâmetros da soma devem ser numéricos.")

        ret = json.dumps({'resultado': par1 + par2,
                          'operacao': "soma",
                          'mensagem': "Obrigado pela chamada de API",
                          'autor': "Elthon Manhas de Freitas"}, cls=NpEncoder)
        return app.response_class(response=ret, status=200, mimetype='application/json')
    except Exception as err:
        ret = json.dumps({"error_message": str(err)})
        return app.response_class(response=ret, status=500, mimetype='application/json')

if __name__ == '__main__':
    print(f"Sou o processo server, id: {os.getpid()}, thread: {threading.current_thread().ident}")
    app.run(port=8080, host='0.0.0.0')


