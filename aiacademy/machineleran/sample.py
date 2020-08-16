from sklearn import datasets
from sklearn import svm
from sklearn import metrics
import matplotlib.pyplot as plt

digits = datasets.load_digits()
print(dir(digits))

digits = datasets.load_digits()
print(digits.data)
print(digits.data.shape)
print(digits.target.shape)

print(len((digits.data[0])))
print(digits.data[0])

print(digits.data[0].shape)

import numpy as np
img = np.reshape(digits.data[0], (8,8))
plt.imshow(img, cmap=plt.cm.gray_r, interpolation='nearest')
plt.axis('off')
plt.show()

num = len(digits.data)
print("num=" + str(num))

images_and_lables = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_lables[:10]):
    plt.subplot(2, 5, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Traning: %i' % label)
plt.show()
