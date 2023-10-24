import numpy as np
from sklearn.metrics import pairwise_distances
from sklearn.cluster import KMeans
import pandas as pd

df = pd.read_excel('C:/Users/felip/OneDrive/Documentos/ProjetoPesquisaMD/grupos/Agrupamento.xlsx')

def davies_bouldin_index(data, labels): # -> Index de Davies Bouldin
    n_clusters = len(np.unique(labels))
    cluster_centers = [np.mean(data[labels == i], axis=0) for i in range(n_clusters)]

    cluster_distances = pairwise_distances(cluster_centers)

    db_indices = []

    for i in range(n_clusters):
        other_clusters = list(range(0, i)) + list(range(i+1, n_clusters))
        cluster_i_std = np.std(data[labels == i], axis=0)
        ratios = []

        for j in other_clusters:
            ratio = (cluster_i_std + np.std(data[labels == j], axis=0)) / cluster_distances[i, j]
            ratios.append(ratio)

        db_indices.append(np.max(ratios))

    return np.mean(db_indices)

X = df.div(df.sum(axis=1), axis='rows') # -> Normalização dos dados (É importante ter para usar o algoritmo)

kmeans = KMeans(n_clusters=10, random_state=0, n_init=10) # -> Aplicação do algoritmo do KMeans
predicted_labels = kmeans.fit_predict(X) # -> Faz parte do algoritmo que Erick mandou, o "X" é o data frame com os dados normalizados

db_index = davies_bouldin_index(X, predicted_labels) # -> Calculando o db_index

print("Índice de Davies-Bouldin:", db_index)