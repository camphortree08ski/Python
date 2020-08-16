from sklearn import datasets
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

# データセットの読み込み
boston = datasets.load_boston()

#  RMを取り出し、 (1, -1) もしくは(-1, 1) を指定することで2次元の横ベクトル及び縦ベクトルを作成 (Scikit-leranのfit()に渡せる形へ変換)
x_train = boston.data[:, 5].reshape(-1, 1)
y_train = boston.target

model = linear_model.LinearRegression()
model.fit(x_train, y_train)

# テストデータの作成
x_test = DataFrame(np.arange(x_train.min(), x_train.max(), 0.1))
prices_test = model.predict(x_test)

# グラフの描画
plt.scatter(x_train, y_train, c="b", alpha=0.5)
plt.plot(x_test, prices_test, c="r")
plt.title("Boston House Prices datase: ")
plt.xlabel("rooms")
plt.ylabel("price $1000's")
plt.show()


# 下記コードは上記コードと同様ですが、PandasのDataFrameに変換したプログラムです。
# PandasのDataFrame型に変換することで、データを扱いやすいようにしています。

#from sklearn import datasets
#from sklearn import linear_model
#import numpy as np
#import matplotlib.pyplot as plt
#from pandas import DataFrame
#%matplotlib inline
#
## データセットの読み込み
#boston = datasets.load_boston()
#
#boston_df = DataFrame(boston.data)
#boston_df.columns = boston.feature_names
#boston_df["Price"] = boston.target # 単回帰モデルを作るため、部屋数のデータを抜き出しています。
#print(boston_df[:10])
#
## 訓練データの作成
#rooms_train = DataFrame(boston_df["RM"])
#y_train = boston.target
#
#model = linear_model.LinearRegression()
#model.fit(rooms_train, y_train)
#
## 部屋数のテストデータの作成
#rooms_test = DataFrame(np.arange(rooms_train.min(), rooms_train.max(), 0.1))
#prices_test = model.predict(rooms_test)
#
## グラフの描画
#plt.scatter(rooms_train, y_train, c="b", alpha=0.5)
#plt.plot(rooms_test, prices_test, c="r")
#plt.title("Boston House Prices datase: ")
#plt.xlabel("rooms")
#plt.ylabel("price $1000's")
#plt.show()
