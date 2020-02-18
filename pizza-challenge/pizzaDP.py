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

info      = D1
S = np.flip(D2, 0).astype(int)
mx = info[0].astype(int)
N = info[1].astype(int)

print(info)
print(S)
print(mx)

# def knapSack1(W , wt , n): 
  
#     if n == 0 or W == 0 : 
#         return 0
  
#     if (wt[n-1] > W): 
#         return knapSack1(W , wt , n-1) 
  
#     else: 
#         return max(wt[n-1] + knapSack1(W-wt[n-1] , wt , n-1), knapSack1(W , wt , n-1)) 

def knapSack2(w, mx, n):
    m = np.zeros((n+1,mx+1))

    for i in range(1,n+1):
        for j in range(1,mx+1):
            if w[i-1] > j :
                m[(i, j)] = m[(i-1, j)]
            else:
                m[(i, j)] = max(m[(i-1, j)], m[(i-1, j-w[i-1])] + w[i-1])

    return m[(n,mx)]

# M1 = knapSack1(mx, S , N) 
M2 = knapSack2(S, mx, N) 

# print(M1)
# print(M1/mx)
print(M2)
print(M2/mx)