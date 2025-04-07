# -*- coding: utf-8 -*-
"""LR_2_task_3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ByygT2ddFIr8IJDcJxmQYONloJyBaNII
"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.datasets import load_iris

# Завантаження набору даних iris
iris = load_iris()
X = iris.data
y = iris.target
df = pd.DataFrame(X, columns=iris.feature_names)
df['class'] = iris.target

# Друк базової інформації
print("Назви класів:", iris.target_names)
print("Назви ознак:", iris.feature_names)
print("Розмірність:", X.shape)
print(df.head())

# 📊 Boxplot
df.drop('class', axis=1).plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.suptitle("Boxplot ознак")
plt.show()

# 📊 Histogram
df.drop('class', axis=1).hist()
plt.suptitle("Histogram ознак")
plt.show()

# 📊 Scatter matrix
scatter_matrix(df.drop('class', axis=1))
plt.suptitle("Scatter matrix ознак")
plt.show()

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# Розділення на X та y
X = df.drop('class', axis=1).values
y = df['class'].values

# Розділення на тренувальну та валідаційну вибірку
X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size=0.2, random_state=1)

# Побудова моделей
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

# Оцінка моделей
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %.2f (±%.2f)' % (name, cv_results.mean(), cv_results.std()))

# Порівняння моделей графіком
plt.boxplot(results, labels=names)
plt.title('Порівняння алгоритмів')
plt.ylabel('Точність (Accuracy)')
plt.grid(True)
plt.show()

import numpy as np

# 🔮 Прогноз нової квітки
X_new = np.array([[5, 2.9, 1, 0.2]])
prediction = model.predict(X_new)
print("\nПрогноз для нової квітки:", prediction[0])
print("Це сорт:", iris.target_names[prediction[0]])