import cPickle as pickle
class Board:
	def __init__(self, num_rows, num_cols):
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.board = []

	def __str__(self):
		return str([" ".join(str(row)) for row in self.board])
		
	def __getitem__(self, tup):
		row = tup[0]
		col = tup[1]
		return self.board[row][col]

	def __setitem__(self, tup, value):
		row = tup[0]
		col = tup[1]
		self.board[row][col] = value

	def create_board(self):
		for rows in range(self.num_rows):
			self.board.append([-1] * self.num_cols)

	def print_board(self):
		for row in self.board:
			print (((" ".join(str(row))).replace(",", "")).replace("[", "")).replace("]", "")

	def save_board(self):
		output = open('saved_board.pickle', 'wb')
		pickle.dump(self.board, output)
		output.close()

	def load_board(self):
		input = open('saved_board.pickle', 'rb')
		self.board = pickle.load(input)
		input.close()
