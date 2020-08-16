# データの分割による性能評価と回帰の評価
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import linear_model

# データセットの読み込み
boston = datasets.load_boston()

#  RMを取り出し、 (1, -1) もしくは(-1, 1) を指定することで2次元の横ベクトル及び縦ベクトルを作成 (scikit-leranのfit()に渡せる形へ変換)
x_train = boston.data[:, 5].reshape(-1, 1)
y_train = boston.target

x_train, x_test, y_train, y_test = train_test_split(x_train, y_train,
test_size = 0.3, random_state=0)

# 学習用データでパラメータ推定
model = linear_model.LinearRegression()
model.fit(x_train, y_train)
# 作成したモデルから予測（学習用、検証用モデル使用）
y_train_pred = model.predict(x_train)
y_test_pred = model.predict(x_test)

# 性能評価
from math import sqrt
# 二乗平均平方根誤差(RMSE)を算出
print('RMSE Test :' + str((sqrt(mean_squared_error(y_test, y_test_pred)))))
# 学習用、検証用データに関してR^2を出力 (回帰モデルの場合score()を使うことで決定係数が得られます。)
print('R^2 Train : %.3f, Test : %.3f' % (model.score(x_train, y_train), model.score(x_test, y_test)))
