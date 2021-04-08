import pygame
from.constants import BLACK, ROWS, WHITE, SQUARE_SIZE, COLS, RED, BROWN, GREEN
from.piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.green_left = 10
        self.create_board()

    # drawing the board
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2 ):
                pygame.draw.rect(win, BROWN, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # move method
    def move(self, row, col):
        pass

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, RED))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, GREEN))
                    else:
                        self.board[row].append(0)  # blank space
                else:
                    self.board[row].append(0)

    # drawing all the pieces in the squares
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
