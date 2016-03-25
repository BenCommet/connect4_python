import cPickle as pickle
import sys
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

def main(arguments):
	if len(arguments) > 4:
		print "Sorry, there were too many arguments."
		print "You only need to include the number of rows, columns and the required length to win."
		print "In that order."
		return 0		
	elif len(arguments) < 4:
		print "Sorry, there were not enough arguments"
		print "You need to include number of rows, columns and the required length to win the game."
		print "In that order."
		return 0

	try:
		num_rows = int(arguments[1])
		num_cols = int(arguments[2])
		length_to_win = int(arguments[3])
	except ValueError:
		print "Please input only numbers"
		return 0

	print "Welcome to Connect 4 in python!"
	load_or_save = str(raw_input("Would you like to continue your old game? Yes or no? :"))
	if load_or_save.lower() == 'yes':
		board = Board(0,0)
		board.load_board()
	else:
		board = Board(num_rows, num_cols)
		board.create_board()
	engine = Engine(num_rows, num_cols, length_to_win, board)
	board.print_board()
	while(1):
		try:
			player_number = int(raw_input("Enter the number of players: "))
			if player_number < 1:
				print "Please use a number larger than 0!"
			else:
				break
		except ValueError:
			print "Please use a number!"
	print "If at any time you would like to save your game, simply type save."
	while (True):
		for player in range(player_number):
			column = -1
			input = raw_input("Pick a column for your token player %d: " % (player))
			if input.lower() == 'save':
				board.save_board()
				print "Your game has been saved."
				return 0
				break
			try:
				column = int(input)
				print engine.place_token(column, player)
			except ValueError:
				print "You didn't save or use an acceptable number. You're turn is over."
			board.print_board()
			if engine.winner() != -1:
				print "Congratulations player %d!!\nYou won conncect 4!" %(player)
				return 0

main(sys.argv)
