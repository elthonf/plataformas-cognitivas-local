import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.ensemble import RandomForestRegressor as rfr
import joblib
# from sklearn.metrics import accuracy_score
import random

def get_a_funnyName():
    f = open("../../datasets/funnynames.txt", "r")
    nomes = f.readlines()
    return random.choice(nomes).rstrip('\n')


if __name__ == "__main__":
    # Carrega os dados
    mydf = pd.read_csv('../../datasets/BaseDefault01.csv')

    # Identifica no dataset as variáveis independentes e a variavel alvo
    targetcol = 'default'
    y = mydf[targetcol]

    # Cria o Classifier (modelo 1)
    independentcols = ['renda', 'idade', 'etnia', 'sexo', 'casapropria', 'outrasrendas', 'estadocivil', 'escolaridade']
    x = mydf[independentcols]

    experimento = mlflow.get_experiment_by_name('Risco de Credito')
    if experimento is None:
        mlflow.create_experiment('Risco de Credito')
        experimento = mlflow.get_experiment_by_name('Risco de Credito')


    for i in range(15):
        runName = "Classificador.. " + get_a_funnyName()
        print("Experiment: " + runName)

        try:

            with mlflow.start_run( experiment_id=experimento.experiment_id, run_name=runName):
                from sklearn.ensemble import RandomForestClassifier as rfc

                if random.randint(1, 3) == 1:
                    raise Exception("Um erro qualquer")

                clf = rfc(n_estimators=random.randint(10, 50),
                          min_samples_leaf=random.randint(1, 5),
                          max_depth=None if random.randint(1, 2) == 1 else random.randint(10, 100)
                          )
                clf.fit(X=x, y=y)

                clf.independentcols = independentcols
                clf_acuracia = clf.score(X=x, y=y)
                print("Modelo 01 (classificador), criado com acurácia de: [{0}]".format(clf_acuracia))

                mlflow.log_param("criterion", clf.criterion)
                mlflow.log_param("n_estimators", clf.n_estimators)
                mlflow.log_param("min_samples_leaf", clf.min_samples_leaf)
                mlflow.log_param("max_depth", clf.max_depth)
                mlflow.log_metric("acuracia", clf_acuracia )
                mlflow.log_metric("minha métrica customizada", 10)

                mlflow.sklearn.log_model(clf, "modelo_mlf")

                pass
        except Exception as err:
            print("Experimento com erro: " + str(err))
            pass

    pass