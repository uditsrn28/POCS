from sklearn import linear_model

clf = linear_model.LinearRegression()
# it contains two arguments out of which one is multi dimensional array
# this multidimensional array has values as
# a1 = m1x1 + m2x2 + m3x3
# a2 = m1x1 + m2x2 + m3x3
# a3 = m1x1 + m2x2 + m3x3
# clf.fit([[x1, x1,x1], [x2, x2,x2], [x3, x3,x3]], [a1,a2,a3])

# equation for the example is
# 0 = m10 + m21 + m32
# 0 = m10 + m21 + m32
# 0 = m10 + m21 + m32
# clf.fit([[x1, x1,x1], [x2, x2,x2], [x3, x3,x3]], [a1,a2,a3])

clf.fit([[0, 0, 0], [1, 1, 1], [2, 2, 2]], [0, 0, 0])
print(clf.coef_)
