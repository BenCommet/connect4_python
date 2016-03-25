from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
from board import Board
from Engine import Engine
import sys

def main():  
    app 	= QApplication(sys.argv)
    table 	= QTableWidget()
    tableItem = QTableWidgetItem()
    board = Board(10, 10)
    board.create_board()
    table.setWindowTitle("Set QTableWidget Header Alignment")
    table.setColumnCount(board.num_cols)
    table.setRowCount(board.num_rows)
    
    table.setHorizontalHeaderLabels(QString("HEADER 1;HEADER 2;HEADER 3;HEADER 4").split(";"))

    table.setItem(0,0, QTableWidgetItem("THIS IS LONG TEXT 1"))
    for row in range(board.num_rows):
    	for col in range(board.num_cols):
    		print board[row, col]
    		table.setItem(row, col, QTableWidgetItem(str(board[row, col])))
	  
    
    table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
    table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
    table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)    
    table.resizeColumnsToContents();
    
    table.show()
    return app.exec_()

if __name__ == '__main__':
    main()
