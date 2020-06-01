import pandas as pd
import json
import numpy as np
from flask import Flask, jsonify, request

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

def intTryParse(value, default: int = 0):
    try:
        return int(value), True
    except ValueError:
        return default, False

@app.route("/", methods=['GET', 'POST'])
def call_home(request = request):
    print(request.values)
    return "SERVER IS RUNNING!"

@app.route("/getclient", methods=['GET', 'POST'])
def getclient(request = request):
    print(request.values)

    mydf = pd.read_csv('../../datasets/BaseUnknown02.csv')

    args = request.args
    qtde = args.get('qtde', '1')
    qtde_int = intTryParse(qtde, default=1)[0]
    if qtde_int <= 0:
        qtde_int = 1
    elif qtde_int >= 10:
        qtde_int = 10

    # Filtra alguns para testes:
    filtrados = mydf.sample(qtde_int)

    return jsonify(filtrados.to_json())


if __name__ == '__main__':
    # app.run(port=8081, host = '0.0.0.0')
    app.run(port=8081)
    pass


