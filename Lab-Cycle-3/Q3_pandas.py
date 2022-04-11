import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


data = pd.read_csv('Iris.csv')
print(data)
data.Species.value_counts().plot(figsize = (10,6), kind = 'bar',color = 'blue')
plt.show()

#data = data.iloc[:, 1:5].to_numpy().transpose()
#data_setosa = data[data.Species == "Iris-setosa"].iloc[:, 1:5].to_numpy().transpose()
#data_versicolor = data[data.Species == "Iris-versicolor"].iloc[:, 1:5].to_numpy().transpose()
#data_virginica = data[data.Species == "Iris-virginica"].iloc[:, 1:5].to_numpy().transpose()
pca = PCA(n_components=2)
for flower_type in ("Iris-setosa", "Iris-versicolor", "Iris-virginica"):
    data_flower = data[data.Species == flower_type].iloc[:, 1:5].to_numpy().transpose()
    pca.fit(data_flower)
    plt.scatter(pca.components_[0],pca.components_[1],c='r')

#pca.fit(data)
#print(pca.components_)


#plt.scatter(pca.components_[0],pca.components_[1],c='r')

plt.show()