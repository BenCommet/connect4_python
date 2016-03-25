import sys
from PyQt4 import QtGui
from board import Board
from Engine import Engine

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
layout = QtGui.QGridLayout()

buttons = {}
board = Board(10, 10)
board.create_board()

label = QtGui.QLabel("label1")
layout.addWidget(label)

for row in range(board.num_rows + 1):
    for col in range(board.num_cols):
        if row == 0:
            buttons[(row, col)] = QtGui.QPushButton('column %d' % (col))
            layout.addWidget(buttons[(row, col)], row, col)
        else:
            buttons[(row, col)] = QtGui.QPushButton('%d' % (board[row -1, col]))       # add to the layout
            layout.addWidget(buttons[(row, col)], row, col)

widget.setLayout(layout)
widget.show()
sys.exit(app.exec_())