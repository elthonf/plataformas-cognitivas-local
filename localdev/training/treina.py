import pandas as pd
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.ensemble import RandomForestRegressor as rfr
from sklearn.ensemble import GradientBoostingClassifier as gbc
from sklearn.ensemble import GradientBoostingRegressor as gbr
import joblib
# from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
if __name__ == "__main__":
    # Carrega os dados
    mydf = pd.read_csv('../../datasets/BaseDefault01.csv')

    # Identifica no dataset as variáveis independentes e a variavel alvo
    targetcol = 'default'
    y = mydf[targetcol]

    independentcols = ['renda', 'idade', 'etnia', 'sexo', 'casapropria', 'outrasrendas', 'estadocivil', 'escolaridade']
    X = mydf[independentcols]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=10)

    # Cria o Classifier (modelo 1)
    independentcols_m1 = ['renda', 'idade', 'etnia', 'sexo', 'casapropria', 'outrasrendas', 'estadocivil', 'escolaridade']
    clf = rfc()
    # Opção de Classificador (comentada):
    #clf = gbc(n_estimators=300, max_depth=5, learning_rate=0.3  )
    clf.fit(X=X_train[independentcols_m1], y=y_train)
    clf.independentcols = independentcols_m1
    clf_acuracia = clf.score(X=X_test[independentcols_m1], y=y_test)
    print("Modelo 01 (classificador), criado com acurácia de: [{0}]".format(clf_acuracia))

    # Cria o Regressor (modelo 2)
    independentcols_m2 = ['renda', 'idade', 'sexo', 'casapropria', 'outrasrendas', 'estadocivil', 'escolaridade']
    rgs = rfr()
    # Opção de Regressor (comentada):
    #rgs = gbr(n_estimators=300, max_depth=5, learning_rate=0.3 )
    rgs.fit(X=X_train[independentcols_m2], y=y_train)
    rgs.independentcols = independentcols_m2
    rgs_acuracia = rgs.score(X=X_test[independentcols_m2], y=y_test)
    print("Modelo 02 (Regressor), criado com acurácia de: [{0}]".format(rgs_acuracia))

    # Salva ambos os modelos
    joblib.dump(clf, '../models/modelo01.joblib')
    print("Modelo 01 (classificador) salvo com sucesso.")
    joblib.dump(rgs, '../models/modelo02.joblib')
    print("Modelo 02 (regressor) salvo com sucesso.")
    pass
