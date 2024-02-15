'''
This is the agent class that we'll be implementing our minimax algorithm in
'''
from Node import ChessNode

class Agent:
    def __init__(self, gameStart, depth, engine, evaluator):
        self.engine = engine
        self.root = ChessNode(engine.createBoardFromFen(gameStart),
                              None,
                              0)
        self.depth = depth
        self.player = self.root.state.turn
        self.engine = engine
        self.evaluator = evaluator
        self.MIN = -float('inf')
        self.MAX = float('inf')
        self.MATE_THRESHOLD = 999000000
        self.MATE_SCORE = 1000000000

    def setStart(self, board):
        self.root = ChessNode(board,
                              None,
                              0)
        self.player = self.root.state.turn

    # This function creates the children of a node using the ChessEngine class
    # If the node is a fringe node, the children have their heuristic score computed
    # note here that the depth convention is opposite to the standard notation - a depth of 0 means a leaf
    def expandNode(self, node, depth):
        if depth == 1:
            return node.generateWithHeuristic(self.engine, self.evaluator)
        else:
            return node.generateWithoutHeuristic(self.engine, self.evaluator)

    # This is a helper class to wrap around the output
    def getMinimaxMoveSequence(self):
        score, movesWithRoot = self.h_minimax(self.depth, self.root, True, self.MIN, self.MAX)
        if (len(movesWithRoot) > 0) and (movesWithRoot[0] == None):
            return movesWithRoot[1:]
        return movesWithRoot
    
    '''
    This is the function you must complete
    Inputs -
    1. self (Agent object reference)
    2. depth (int)
    3. node (chessNode)
    4. maximizingPlayer (bool)
    5. alpha (float)
    6. beta (float)
    
    Outputs -
    1. score (float)
    2. moves (list(string))
    
    Note - we use depth here to measure how far down we need to keep going, we stop at depth = 0
    '''

    def h_minimax(self, depth, node, maximizingPlayer, alpha, beta):
        # Your solution goes here!
