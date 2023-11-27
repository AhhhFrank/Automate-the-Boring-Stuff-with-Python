#! python3
# chessDictValidator.py
# Arthur: Frank Lee
# Date: 11/26/23
###
# In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board. 
# Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.
# A valid board will have exactly one black king and exactly one white king. 
# Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. 
# The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. 
# This function should detect when a bug has resulted in an improper chess board.
###

import sys



# TODO check valid space from 1a to 8h
# loop through keys and check the x and y axis if they are in bounds (against a set list x and y values)
def check_board_space(board):
	x_axis = ['1', '2', '3', '4', '5', '6', '7', '8']
	y_axis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	for k in board.keys():
		if k[0] not in x_axis:
			return False
		if k[1] not in y_axis:
			return False
	return True

# TODO check if game piece starts with w or b then the game piece (king, queen, pawn, knight, bishop, or rook)
# loop through values and check if they start with w or b then a game piece (against a set list of pieces)
def check_game_pieces(board):
	gamepieces = ['king', 'queen', 'pawn', 'knight', 'bishop', 'rook']
	for v in board.values():
		if v[0] != 'w' and v[0] != 'b':
			return False
		if v[1:] not in gamepieces:
			return False
	return True

# TODO check if 2 kings (w & b)
# count exactly 1 white king and 1 black king
def check_kings(board):
	wking = 0
	bking = 0
	for v in board.values():
		if v == 'wking':
			wking += 1
		if v == 'bking':
			bking += 1
	if wking == 1 and bking == 1:
		return True
	else:
		return False

# TODO check at most 8 pawns
# count at most 8 pawns for each side
def count_pawns(board):
	wpawns = 0
	bpawns = 0
	for v in board.values():
		if v == 'wpawn':
			wpawns += 1
		if v == 'bpawn':
			bpawns += 1
	if wpawns <= 8 and bpawns <= 8:
		return True
	else:
		return False	

# TODO check each side has at most 16 pieces
# count values up to 16 starting with w or b
def count_pieces(board):
	wpieces = 0
	bpieces = 0
	for v in board.values():
		if v[0] == 'w':
			wpieces += 1
		if v[0] == 'b':
			bpieces += 1
	if wpieces <= 16 and bpieces <= 16:
		return True
	else:
		return False

# TODO if error then return message for error
# TODO chessboard input  
def is_valid_chess_board(board):
	if check_board_space(board) and check_game_pieces(board) and check_kings(board) and count_pawns(board) and count_pieces(board):
		return True
	else:
		return False


def main():
	#board = {'1a': 'wking', '2b': 'bking', '1b': 'bpawn', '1c': 'bpawn', '1d': 'bpawn', '1e': 'bpawn', '1f': 'bpawn', '1g': 'bpawn'}
	board = {'1a': 'wking', '2b': 'bking', '1b': 'bpawn', '1c': 'bpawn', '1d': 'bpawn', '1e': 'bpawn', '1f': 'bpawn', '1g': 'bpawn', '1h': 'bpawn', '2a': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn', '3a': 'bpawn', '3b': 'bpawn', '3c': 'bpawn', '3d': 'bpawn', '3e': 'bpawn', '3f': 'bpawn', '3g': 'bpawn', '3h': 'bpawn', '4a': 'bpawn'}
	print(is_valid_chess_board(board))


if __name__ == '__main__':
	sys.exit(main())
