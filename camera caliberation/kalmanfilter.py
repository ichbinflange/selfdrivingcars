from re import T
import numpy as np

p_pred = np.array( [[0.35,0.5],[0.5,1.1]])
H = np.array([1,0])

print(p_pred.shape)
print(H.T.shape)

K_1 = p_pred.dot(H.T)
K_2 = H.dot(p_pred).dot(H.T)+ 0.05

K_3= 1/K_2

print(K_1*K_3)