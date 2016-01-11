from sklearn import linear_model
import numpy as np

x1 = np.array(["puma", 1, 1, 1, 1])
x2 = np.array(["lee", 2, 2, 2, 2])
x3 = np.array(["puma", 3, 3, 3, 3])
x4 = np.array(["lee", 4, 4, 4, 4])
x5 = np.array(["puma", 5, 5, 5, 5])
x6 = np.array(["cooper", 6, 6, 6, 6])
x7 = np.array(["puma", 7, 7, 7, 7])
x8 = np.array(["levis", 8, 8, 8, 8])
results = np.array([1, 2, 3, 4, 5, 6, 7, 8])

clf = linear_model.LinearRegression()
clf.fit([x1, x2, x3, x4, x5, x6, x7, x8], results)
print(clf.coef_)
