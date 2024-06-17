import numpy as np

def entropy(labels):
    # Calcula as proporções de cada classe
    _, counts = np.unique(labels, return_counts=True)
    probabilities = counts / counts.sum()
    
    # Calcula a entropia
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

# Exemplo de uso
labels = ['False', 'False', 'False', 'True', 'True', 'True', 'True', 'True']
result = entropy(labels)
print("Entropia: {result}")
