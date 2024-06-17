from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Carregar o dataset Iris
data = load_iris()
X = data.data
y = data.target

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Construir o classificador de árvore de decisão
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X_train, y_train)

# Previsão e avaliação
y_pred = clf.predict(X_test)
accuracy = np.mean(y_pred == y_test)
print(f"Accuracy: {accuracy:.2f}")

# Visualizar a árvore de decisão
plt.figure(figsize=(20,10))
tree.plot_tree(clf, filled=True, feature_names=data.feature_names, class_names=data.target_names)
plt.show()
