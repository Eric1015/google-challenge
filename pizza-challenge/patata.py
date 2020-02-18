# import numpy as np

# res = np.load("a_example.in", allow_pickle=True)

# print(res)

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

f = open(input_file, "r")

S = []
it = 0
for x in f:
    if it == 0:
        M = int(x.split(" ")[0])
        N = int(x.split(" ")[1])
    else:
        for i in x.split(" "):
            S.append(int(i))
    it += 1

currentM = M
index = N - 1
res = []

while currentM > 0 and index >= 0:
    if currentM - S[index] >= 0:
        currentM -= S[index]
        res.append(index)
    index -= 1

res.reverse()

f = open(output_file, "w")
f.write(str(len(res)) + " \n" + " ".join(str(x) for x in res) + " \n")
f.close()