class Engine:
	def __init__(self, num_rows, num_cols, length_to_win, board):
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.length_to_win = length_to_win
		self.board = board

	def check_horizontal(self):
		for row in range(self.num_rows):
			count = 0
			player = -1
			for col in range(self.num_cols):
				if self.board[row, col] == -1:
					player = -1
					count = 0
				elif count == 0:					
					count = 1
					player = self.board[row, col]
				elif self.board[row, col] == player:
					count = count + 1
				else:
					count = 1
					player = self.board[row, col]
				if count == self.length_to_win :
					return player
		return -1

	def check_vertical(self):
		for col in range(self.num_cols):
			count = 0
			player = -1
			for row in range(self.num_rows):
				if self.board[row, col] == -1:
					player = -1
					count = 0
				elif count == 0:
					count = 1
					player = self.board[row, col]
				elif self.board[row, col] == player:
					count = count + 1
				else:
					count = 1
					player = self.board[row, col]
				if count == self.length_to_win:
					return player
		return -1

	def check_diagonal_left(self):
		maxRows = self.num_cols + self.num_rows - 2
		count = 0
		player = -1
		for current_row in range(maxRows):
			for row in range(self.num_rows):
				for col in range(self.num_cols):
					if row + col - current_row == 0:
						if self.board[row, col] == -1:
							count = 0
							player = -1
						elif self.board[row, col] != player:
							count = 1
							player = self.board[row, col]
						else:
							count += 1
						if count == self.length_to_win:
							return player
		return -1

	def check_diagonal_right(self):
		player = -1
		for row in range(self.num_rows - self.length_to_win + 1):
			for col in range(self.num_cols - self.length_to_win + 1):
				if self.board[row, col] != -1:
					temp = self.board[row, col]
					flag = 1
					for line in range(self.length_to_win):
						if temp != self.board[row + line, col + line]:
							flag = -1
					if flag == 1:
						return temp
		return -1

	def place_token(self, column, player):
		if column > self.num_cols:
			return -1
		if self.board[0, column] != -1:
			return -1
		for row in reversed(range(self.num_rows)):
			if self.board[row, column] == -1:
				self.board[row, column] = player
				return 1
		return -1

	def winner(self):
		if self.length_to_win < 1:
			return -1
		if self.num_rows < 1 or self.num_cols < 1:
			return -1
		horizontal = self.check_horizontal()
		vertical = self.check_vertical()
		diagonal_right = self.check_diagonal_right()
		diagonal_left = self.check_diagonal_left()
		if horizontal != -1:
			return horizontal
		if vertical != -1:
			return vertical
		if diagonal_right != -1:
			return diagonal_right
		if diagonal_left != -1:
			return diagonal_left
		return -1