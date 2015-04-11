class BichromeBoard:
	def ableToDraw(self, board):
		b = list(board)
		l = []
		ans = 0
		for i in range(len(b)):
			s = list(b[i])
			for j in range(len(s)):
				if s[j] == '?':
					if j-1 >=0:
						if s[j-1] == 'W':
							s[j] = 'B'
						else: s[j] = 'W'
					elif i-1 >=0:
						if b[i-1][j] == 'W':
							s[j] = 'B'
						else: s[j] = 'W'
					elif j+1 < len(s):
						if s[j+1] == 'W':
							s[j] = 'B'
						else: s[j] = 'W'
					elif i+1 < len(b):
						if b[i+1][j] == 'W':
							s[j] = 'B'
						else: s[j] = 'W'
					else:
						s[j] = 'W'
				if j+1 < len(s):
					if s[j] == s[j+1]:
						ans = 1
				if i+1 < len(b):
					if s[j] == b[i+1][j]:
						ans = 1
		if ans == 0:
			return 'Possible'
		else:
			return 'Impossible'
		

s = BichromeBoard()
#x = ("W?W","??B","???")
x = ("W??W",)
print s. ableToDraw(x)
			

