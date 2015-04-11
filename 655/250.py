class BichromeBoard:
	def ableToDraw(self, board):
		color1 = ['W', 'B']
		color2 = ['B', 'W']
		h ,w = len(board), len(board[0])

		ret = all( board[i][j] in [color1[(i+j)%2], '?'] for i in range(h) for j in range(w) ) or all(
				board[i][j] in [color2[(i+j)%2], '?'] for i in range(h) for j in range(w)) 

		if ret: 
			return 'Possible'
		else:
			return 'Impossible'

s = BichromeBoard()
#x = ("W?W","??B","???")
x = ("W??W",)
print s. ableToDraw(x)
			

