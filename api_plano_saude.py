from unittest import result
from flask import Flask, Response, request
from flask_cors import CORS
import json
import os
from modelo.modelo_plano_saude import PlanoSaude


app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

# Página com resultado da previsão
@app.route("/previsao", methods = ["POST"])
def previsao():
    body = request.get_json()
    input_idade = body["idade"]
    classe_plano = PlanoSaude(input_idade)
    idade_plano = classe_plano.prepara_dados()
    resultado_prev = classe_plano.predict(idade_plano)
    imprime_previsao = to_json(input_idade, resultado_prev)
    
    return gera_response(200, 'valor_plano', imprime_previsao, 'Valor previsto calculado')

def to_json(idade, valor):
        return {"idade": idade, "valor": valor}

def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")


if __name__ == '__main__':
    #start Flask
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port = port)