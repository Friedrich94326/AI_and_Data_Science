import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets     # 主題 : 用 KNN 分類鳶尾花
np.random.seed(0)
iris=datasets.load_iris()  # iris=鳶尾花
x=iris.data              # x 設為 iris 的 data
y=iris.target            # y 設為 iris 的 花名
i=np.random.permutation(len(iris.data))   # 把 iris 的 data打亂之後給編號
x_train=x[i[:-10]]       # 設前 140 筆 data 為訓練集
y_train=y[i[:-10]]       # 前 140 筆 花名 為訓練集的答案
x_test=x[i[-10:]]        # 剩下 10 筆 data 為測試集
y_test=y[i[-10:]]        # 剩下 10 筆的答案

from sklearn.neighbors import KNeighborsClassifier   # 叫出 KNN
knn=KNeighborsClassifier()
knn.fit(x_train,y_train)    # 用 Knn 的 fit 函數進行訓練，得出鳶尾花的 KNN分類模型

print(knn.predict(x_test))  # 用資料 x_test 對分類模型 Knn 做測試
print(y_test)               # 比對答案

