import numpy as np

def rueckwaertseinsetzen(A, b):
    x = np.zeros(len(b))
    for j_neg in range(len(b)):
        j = len(b) - j_neg -1
        
        inner_sum = 0
        for k in range(j+1,len(b)):
            inner_sum += A[j, k]*x[k]
        x[j] = 1./A[j,j]*(b[j] - inner_sum)
    return x
