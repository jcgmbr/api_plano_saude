import numpy as np
import joblib

class PlanoSaude:
     # Método construtor
    def __init__(self, idade):
         self.idade = idade
        
   # Método para preparar os dados
    def prepara_dados(self):
        #self.idade = idade
        entrada = np.array(self.idade).reshape(-1,1)
        return  entrada   

     # Método para as previsões
    def predict(self, idade):
        valor_idade = idade
        model = joblib.load('./modelo/modelo_treinado/modelo_plano_saude.pkl')
        predicted_plano_value = model.predict(valor_idade)
        value = predicted_plano_value[0]
        return value
