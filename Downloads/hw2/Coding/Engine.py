'''
This file contains the engine class used for encapuslating the rules of chess
You DO NOT need to modify or edit this file
'''

import chess
import chess.svg
import IPython
from IPython.display import display
import io

# This class abstracts out all the game logic
class ChessEngine:
    
    @staticmethod
    def createBoardFromFen(fen):
        return chess.Board(fen)
    
    @staticmethod
    def listLegalMoves(board):
        return list(map(lambda x: str(x), list(board.legal_moves)))
    
    @staticmethod
    def generateBoardStateTuples(board):
        possibleStates = []
        if board.is_checkmate() or board.is_game_over():
            return []
        for move in board.legal_moves:
            childState = chess.Board(board.fen())
            childState.push(move)
            possibleStates.append((childState, move))
        return possibleStates
    
    @staticmethod
    def renderBoard(board):
        htmlToRender = chess.svg.board(board,
                                       size=500)
        display(IPython.display.HTML(htmlToRender))

    @staticmethod
    def executeMove(board, move):
        board.push(chess.Move.from_uci(move))
        return board

    # This function lets you play out a sequence of moves to see how the board changes
    # Use it in a Jupyter Notebook
    def visualizeMoves(self, startingFen, moves):
        board = chess.Board(startingFen)
        print("Start")
        self.renderBoard(board)
        for move in moves:
            print("Move:", move)
            board.push(chess.Move.from_uci(move))
            if board.is_checkmate():
                print("Checkmate!")
            self.renderBoard(board)
