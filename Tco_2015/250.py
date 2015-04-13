class Similars:
	def getNum(self, x, y):
		ans = 0
		p = set(x)
		q = set(y)
		for i in p:
			if i in q:
				ans += 1
		return ans
	def getList(self, x):
		l = []
		while x > 0:
			l.append(x%10)
			x /= 10
		l = sorted(l)
		return list(set(l))
		
	def maxsim(self, L, R):
		f_ans = 0
		ans = 0
		l = []
		for i in range(L, R+1):
			t = self.getList(i)
			l.append(t)
		s = sorted(l)
		print s
		for i in range(len(s)-1):
			ans = self.getNum(s[i],s[i+1])
			if f_ans < ans:
				f_ans = ans
		return f_ans
x = Similars()
L = 998
R = 1013
print x.maxsim(L,R)
