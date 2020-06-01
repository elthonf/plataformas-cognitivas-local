import pandas as pd
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.ensemble import RandomForestRegressor as rfr
from sklearn.ensemble import GradientBoostingClassifier as gbc
from sklearn.ensemble import GradientBoostingRegressor as gbr
import joblib
# from sklearn.metrics import accuracy_score

if __name__ == "__main__":
    # Carrega os dados
    mydf = pd.read_csv('../../datasets/BaseDefault01.csv')

    # Identifica no dataset as variáveis independentes e a variavel alvo
    targetcol = 'default'
    y = mydf[targetcol]

    # Cria o Classifier (modelo 1)
    independentcols = ['renda', 'idade', 'etnia', 'sexo', 'casapropria', 'outrasrendas', 'estadocivil', 'escolaridade']
    x = mydf[independentcols]
    clf = rfc()
    # Opção de Classificador (comentada):
    #clf = gbc(n_estimators=300, max_depth=5, learning_rate=0.3  )
    clf.fit(X=x, y=y)
    clf.independentcols = independentcols
    clf_acuracia = clf.score(X=x, y=y)
    print("Modelo 01 (classificador), criado com acurácia de: [{0}]".format(clf_acuracia))

    # Cria o Regressor (modelo 2)
    independentcols = ['renda', 'idade', 'sexo', 'casapropria', 'outrasrendas', 'estadocivil', 'escolaridade']
    x = mydf[independentcols]
    rgs = rfr()
    # Opção de Regressor (comentada):
    #rgs = gbr(n_estimators=300, max_depth=5, learning_rate=0.3 )
    rgs.fit(X=x, y=y)
    rgs.independentcols = independentcols
    rgs_acuracia = rgs.score(X=x, y=y)
    print("Modelo 02 (Regressor), criado com acurácia de: [{0}]".format(rgs_acuracia))

    # Salva ambos os modelos
    joblib.dump(clf, '../models/modelo01.joblib')
    print("Modelo 01 (classificador) salvo com sucesso.")
    joblib.dump(rgs, '../models/modelo02.joblib')
    print("Modelo 02 (regressor) salvo com sucesso.")
    pass
