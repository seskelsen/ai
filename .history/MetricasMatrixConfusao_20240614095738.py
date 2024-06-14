# Resultados de exemplo
resultados = [
    {"real": "positivo", "predito": "positivo"},
    {"real": "negativo", "predito": "positivo"},
    {"real": "positivo", "predito": "negativo"},
    {"real": "negativo", "predito": "negativo"}
    # Adicione mais resultados aqui...
]

# Inicializando contadores
TP, FN, FP, TN = 0, 0, 0, 0

# Contando os valores
for resultado in resultados:
    if resultado["real"] == "positivo":
        if resultado["predito"] == "positivo":
            TP += 1
        else:
            FN += 1
    else:
        if resultado["predito"] == "positivo":
            FP += 1
        else:
            TN += 1

# Criando a matriz de confusão
matriz_confusao = [
    [TP, FN],
    [FP, TN]
]

# Calculando as métricas
acuracia = (TP + TN) / (TP + FN + FP + TN)
precisao = TP / (TP + FP)
revocacao = TP / (TP + FN)
f1_score = 2 * (precisao * revocacao) / (precisao + revocacao)

# Exibindo os resultados
print("Matriz de Confusão:", matriz_confusao)
print("Acurácia:", acuracia)
print("Precisão:", precisao)
print("Revocação:", revocacao)
print("F1-Score:", f1_score)
