curl --location --request POST 'http://localhost:8080/modelo01' \
--header 'Content-Type: application/json' \
--data-raw '{
"renda":{"1":4592.7743118684},
"idade":{"1":48.2306622957},
"etnia":{"1":1},
"sexo":{"1":0},
"casapropria":{"1":1},
"outrasrendas":{"1":0},
"estadocivil":{"1":1},
"escolaridade":{"1":2},
"default":{"1":0}
}
'