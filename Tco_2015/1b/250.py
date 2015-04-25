import math
class TheNicePair:
    def getSet(self, i, j, A):
        l = []
        for p in range(i, j+1):
            for m in range(1, int(math.sqrt(A[p]) + 1)):
                if A[p] % m == 0:
                    l.append(A[p]/m)
                    l.append(m)
        s = set(l)
        s.remove(1)
        print s
        return s 

    def solve(self, A):
        k = -1
        for i in range(0,len(A)):
            for j in range(i,len(A)):
                l = self.getSet(i , j, A)
                for v in l:
                    num = 0
                    for p in range(i,j+1):
                        if A[p] % v == 0:
                            num += 1
                    if num / (j - i + 1.0)  >= 0.5:
                        print j-i
                        if k < (j - i):
                            k = j - i 
        return k

s = TheNicePair()
A = (1,)
print s.solve(A)
