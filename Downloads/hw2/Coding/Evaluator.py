'''
This file contains the evaluator class used for computing the heuristic value of node.
You DO NOT need to modify or edit this file.
'''
import chess
import pickle

class SimplifiedEvaluator:  
    def __init__(self, player, usePromotion = True, useTrade = True, usePST = True):
        self.player = player
        self.piece_value = {chess.PAWN: 100,
                            chess.ROOK: 500,
                            chess.KNIGHT: 500,
                            chess.BISHOP: 500,
                            chess.QUEEN: 900,
                            chess.KING: 20000}

        # The heuristic has three components. These three variables control which ones are active
        self.usePromotion = usePromotion
        self.useTrade = useTrade
        self.usePst = usePST

        self.pieceSquareTable = self.loadPST()
    
    def getScore(self, board, move):
        return self.getMoveScore(board, move, self.checkIfEndgame(board))
        
    def getMoveScore(self, board, move, endgame):
        """
        We have a base score that comprises of the total value of our board minus that of our opponent
        In addition to this, we include 3 parts -
        1. Is there a promotion? This is a good thing
        2. Are we capturing a piece? If so -
            a. we punish capturing a weak piece with a strong piece
            b. we reward capturing a strong piece with a weak one
        3. How has our position changed?
        """

        promotionScore = 0
        if self.usePromotion:
            if move.promotion is not None:
                if board.turn == self.player:
                    promotionScore = 1000
                else:
                    promotionScore -1000


        if self.usePst:
            piece = board.piece_at(move.from_square)
            if piece:
                initialPositionScore = self.getPiecePositionScore(piece, move.from_square, endgame)
                finalPositionScore = self.getPiecePositionScore(piece, move.to_square, endgame)
                positionChangeScore = finalPositionScore - initialPositionScore
        else:
            positionChangeScore = 0

        totalBoardScore = self.evaluateBoard(board, self.player)

        captureScore = 0.0
        if self.useTrade:
            if board.is_capture(move):
                captureScore = self.getCaptureScore(board, move)

        totalMoveValue = captureScore + positionChangeScore
        if board.turn != self.player:
            totalMoveValue = -totalMoveValue

        totalMoveValue += promotionScore
        totalMoveValue += totalBoardScore

        return totalMoveValue
        
    def getCaptureScore(self, board, move):
        if board.is_en_passant(move):
            return self.piece_value[chess.PAWN]

        target = board.piece_at(move.to_square)
        attacker = board.piece_at(move.from_square)
        return self.piece_value[target.piece_type] + (self.piece_value[target.piece_type]
                                                      - self.piece_value[attacker.piece_type])
        
    def getPiecePositionScore(self, piece, square, endgame):
        piece_type = piece.piece_type
        if piece_type == chess.KING:
            return self.pieceSquareTable[(piece.piece_type, piece.color, endgame)][square]
        return self.pieceSquareTable[(piece.piece_type, piece.color)][square]
        
    def evaluateBoard(self, board, player):
        total = 0
        isEndgame = self.checkIfEndgame(board)

        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if not piece:
                continue
            value = self.piece_value[piece.piece_type]
            if self.usePst:
                value += self.getPiecePositionScore(piece, square, isEndgame)
            if piece.color == player:
                total += value
            else:
                total -= value
        return total
        
    def isMinorPiece(self, piece):
        return (piece.piece_type == chess.BISHOP or piece.piece_type == chess.KNIGHT)
        
    def checkIfEndgame(self, board):
        queens = 0
        minorpieces = 0

        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                if piece.piece_type == chess.QUEEN:
                    queens += 1
                elif self.isMinorPiece(piece):
                    minorpieces += 1

        if queens == 0 or (queens == 2 and minorpieces <= 1):
            return True
        return False
    
    def loadPST(self):
        # Dict of form {(chess.piece, chess.color):PST as a list} for non-king pieces
        # {(chess.king, chess.color, isEndgame):PST as a list} for king
        with open('PieceSquareTables.pickle', 'rb') as handle:
            pst = pickle.load(handle)
        return pst
