import numpy as np
import csv

# A = np.load('a_example.csv')
A = np.array(list(csv.reader(open("a_example.csv") )))
A1 = np.loadtxt(A[(0,)], delimiter=' ')
A2 = np.loadtxt(A[(1,)], delimiter=' ')

B = np.array(list(csv.reader(open("b_small.csv"))))
B1 = np.loadtxt(B[(0,)], delimiter=' ')
B2 = np.loadtxt(B[(1,)], delimiter=' ')

C = np.array(list(csv.reader(open("c_medium.csv"))))
C1 = np.loadtxt(C[(0,)], delimiter=' ')
C2 = np.loadtxt(C[(1,)], delimiter=' ')

D = np.array(list(csv.reader(open("d_quite_big.csv"))))
D1 = np.loadtxt(D[(0,)], delimiter=' ')
D2 = np.loadtxt(D[(1,)], delimiter=' ')

E = np.array(list(csv.reader(open("e_also_big.csv"))))
E1 = np.loadtxt(E[(0,)], delimiter=' ')
E2 = np.loadtxt(E[(1,)], delimiter=' ')

M = 0
info      = E1
S = np.flip(E2, 0).astype(int)
mx = info[0].astype(int)
N = info[1].astype(int)

print(info)
print(S)
print(mx)

def knapSack1(S, N, mx): 
    M = 0    
    for i in range(N):
        s = S[i]
        if M + s < mx:
            M += s
        if M == mx:
            break
    return M

def knapSack2(w, n, mx):
    m = np.zeros((n,mx))

    for i in range(n):
        for j in range(mx):
            if w[i] > j :
                m[(i, j)] = m[(i-1, j)]
            else:
                m[(i, j)] = max(m[(i-1, j)], m[(i-1, j-w[i])] + w[i])

    return m[(n-1,mx-1)]

def knapSack(S, N, mx):
    if N < 100:
        return knapSack2(S, N, mx)
    else:
        return knapSack1(S, N, mx)

M = knapSack(S ,N, mx) 

print(M)
print(M/mx)