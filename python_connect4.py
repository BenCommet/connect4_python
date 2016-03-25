from board import Board
from Engine import Engine
import cPickle as pickle
import sys

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
