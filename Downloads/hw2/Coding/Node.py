'''
This file contains the node that we'll be using in our Minimax search algorithm
You DO NOT need to modify or edit this file.
'''
class ChessNode:
    
    def __init__(self, board, previousMove, score, isTerminal=False):
        self.state = board
        self.move = previousMove
        self.score = score

        # The minimax problems we work out in examples have every leaf node at the same depth
        # However, in games like chess, you may run into a situation where a node has no additional children
        # This is an endgame situation - either you've won, lost, or had a draw
        # In order to ensure we account for this, we add a flag to indicate if a node is terminal.
        # A terminal node has no children, and has a score of 0 if tied, and +/- CHECKMATE_SCORE otherwise
        self.isTerminalNode = isTerminal
        self.CHECKMATE_SCORE = 1000000
        
    # Use this function to generate child nodes without the heuristic value
    # While this function isn't really necessary, it saves us time since we only need the
    # heuristic value of the leaf nodes to be computed
    def generateWithoutHeuristic(self, engine, evaluator):
        childStates = engine.generateBoardStateTuples(self.state)
        children = []
        for child in childStates:
            terminal = False
            childBoardState = child[0]
            if childBoardState.is_checkmate():
                terminal = True
                if childBoardState.turn == evaluator.player:
                    score = -self.CHECKMATE_SCORE
                else:
                    score = self.CHECKMATE_SCORE
            elif childBoardState.is_game_over():
                terminal = True
                score = 0
            else:
                score = 0
            children.append(ChessNode(child[0], child[1].uci(), score, terminal))
        return children
        
    # Use this function to generate child nodes with the heuristic value
    def generateWithHeuristic(self, engine, evaluator):
        childStates = engine.generateBoardStateTuples(self.state)
        children = []
        for child in childStates:
            terminal = False
            childBoardState = child[0]
            if childBoardState.is_checkmate():
                terminal = True
                if childBoardState.turn == evaluator.player:
                    score = -self.CHECKMATE_SCORE
                else:
                    score = self.CHECKMATE_SCORE
            elif childBoardState.is_game_over():
                terminal = True
                score = 0
            else:
                score = evaluator.getMoveScore(self.state, child[1], evaluator.player)
            children.append(ChessNode(child[0], child[1].uci(), score, terminal))
        children.sort(reverse=(self.state.turn == evaluator.player), key = lambda x : x.score)
        return children
