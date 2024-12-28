from numpy import loadtxt, sort, isin

A, B = sort(loadtxt('1input.txt', int).T)
print(sum(abs(A - B)),
      sum(isin(B, A) * B))
type(A)