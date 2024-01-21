"""
This file implements the Agent class.
"""
import numpy as np
from queue import Queue, LifoQueue, PriorityQueue
from Maze import Action, Maze
import matplotlib.colors as colors
import matplotlib.pyplot as plt


# First, we define the Node class, that imitates the nodes mentioned in lecture.
# A node represents a step along the way of searching for the goal state in a search tree/graph.
# Remember - a node is not the same as a coordinate. It contains more information
class Node:
    def __init__(self, coord, parent=None, action=None, path_cost=0):
        self.coord = coord
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    # Given a node, get a path back to the start node by recording the actions taken from the parent node
    def trace_back(self):
        coord_path = []
        actions = []
        trace: Node = self
        while trace is not None:
            coord_path.append(trace.coord)
            if trace.action is not None:
                actions.append(trace.action)
            trace = trace.parent
        coord_path.reverse()
        actions.reverse()
        return coord_path, actions

    # Algorithms like UCS require us to compare and order nodes
    # Since nodes are objects, we can define a custom comparator via operator overriding
    # The three functions below override the standard "==", "<" and ">" operators for the node class
    # This allows us to implement logic like node1 > node2
    # More importantly, these operators are used by the queue data structures we imported at the start
    def __eq__(self, other):
        return self.path_cost == other.path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def __gt__(self, other):
        return self.path_cost > other.path_cost


# Next we define the AStar node. Note that the AStar node is identical to a regular node but has two key differences
# 1. The AStar node has an end coordinate
# 2. The AStar node has a heuristic value, computed using a heuristic function
class AStarNode(Node):
    # HINT: Make sure this is set first before using the heuristics function
    # Remember that you need to set this for the entire class, not just one object
    END_COORDS = None

    def __init__(self, coord, parent=None, action=None, cost=0):
        super().__init__(coord, parent, action, cost)
        # store the heuristics value for this node
        self.h_val = self.heuristic_function()

    # TODO - complete the heuristic function
    # Implement the heuristic function for the AStar Node by returning the minimum euclidean (straight line) distance
    # between the AStar Node's coordinate and the END_COORDS
    # Hint: You may use numpy's sqrt function, and the builtin min function
    def heuristic_function(self):
        # TODO here

        #Calculate euclidean distances
        for x,y in AStarNode.END_COORDS:
            coordX = x - self.coord[0]
            coordY = y - self.coord[1]

            coordXSq = coordX**2
            coordYSq = coordY**2

            eucDist = np.sqrt(coordXSq + coordYSq)
        
        return eucDist

    # TODO - complete the operator overloads for the AStar node class
    # Unlike the regular node, AStar nodes are not compared using just the path costs
    # Complete the operator overloads for the AStar nodes.
    # Hint: You can use the same syntax as the overload in the base node class

    def __eq__(self, other):
        # TODO here
      return self.path_cost == other.path_cost

    def __lt__(self, other):
        # TODO here
        return None

    def __gt__(self, other):
        # TODO here
        return None


# This is the Agent class. This class mimics an agent that explores the maze
# The agent has just two attributes - the maze that it is in, and the node expansion history
# The expansion history is used just to evaluate your implementation
class Agent:
    def __init__(self, maze):
        self.maze = maze
        self.expansion_history = []

    # We want to reset this every time we use a new algorithm
    def clear_expansion_history(self):
        self.expansion_history.clear()

    # Visualize the maze and how it was explored in matplotlib
    def visualize_expansion(self, path):
        plt.subplot(1, 1, 1)
        blocks = np.zeros((self.maze.height, self.maze.width))
        blocks[:] = np.nan
        for co_ord in self.maze.pits:
            blocks[co_ord[1], co_ord[0]] = 2

        expansion_cval = np.zeros((self.maze.height, self.maze.width))

        for i, coord in enumerate(self.expansion_history):
            expansion_cval[coord[1], coord[0]] = len(self.expansion_history) - i + len(self.expansion_history)

        plt.pcolormesh(
            expansion_cval,
            shading='flat',
            edgecolors='k', linewidths=1, cmap='Blues')

        cmap = colors.ListedColormap(['grey', 'grey'])

        plt.pcolormesh(
            blocks,
            shading='flat',
            edgecolors='k', linewidths=1, cmap=cmap)

        start = self.maze.start
        ends = self.maze.end

        # Plot start and end points
        plt.scatter(start[0] + 0.5, start[1] + 0.5, color='red', s=100, marker='o', label='Start')
        for end in ends:
            plt.scatter(end[0] + 0.5, end[1] + 0.5, color='gold', s=100, marker=(5, 1), label='End')

        plt.title("Maze Plot")
        plt.xlabel("X")
        plt.ylabel("Y", rotation=0)

        plt.xticks(np.arange(0 + 0.5, expansion_cval.shape[1] + 0.5), np.arange(0, expansion_cval.shape[1]))
        plt.yticks(np.arange(0 + 0.5, expansion_cval.shape[0] + 0.5), np.arange(0, expansion_cval.shape[0]))

        # Plot the path only if it exists
        if path is not None:
            for i in range(len(path) - 1):
                x, y = path[i]
                next_x, next_y = path[i + 1]
                plt.annotate('', xy=(next_x + 0.5, next_y + 0.5), xytext=(x + 0.5, y + 0.5),
                             arrowprops=dict(color='g', arrowstyle='->', lw=2))
        plt.show()

    # TODO: Complete the goal_test function
    # Input: a node object
    # Returns: A boolean indicating whether or not the node corresponds to a goal
    # Hint: The agent has the maze object as an attribute. The maze object has a set of end coordinates
    # You can use the 'in' operator to determine if an object is in a set
    def goal_test(self, node):
        # Your implementation here :)
        return None

    # TODO: Complete the expand_node function
    # For each neighbouring node that can be reached from the current node within one action, 'yield' the node.
    # Hints:
    # 1.  Use self.maze.valid_ordered_action(...) to obtain all valid action for a given coordinate
    # 2.  Use Maze.resulting_coord(...) to compute the new states. Note the capital M is important, since it's a
    #     class function
    # 3.  Use yield to temporarily return a node to the caller function while saving the context of this function.
    #     When expand is called again, execution will be resumed from where it stopped.
    #     Follow this link to learn more:
    #     https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
    # 3.  Take advantage of polymorphic construction. You need to ensure that a Node object yields Node objects, while
    #     an AStarNode object yields AStarNodes. You can use type(node) to do this.
    def expand_node(self, node):
        self.expansion_history.append(node.coord)
        s = node.coord
        for action in self.maze.valid_ordered_action(s):
            # TODO Here
            # Use the maze object's resulting_coord function to compute the new state after taking the action
            # Compute the new cost of getting to this state via the current path and action
            new_state = None
            new_cost = 0
            yield type(node)(new_state, node, action, new_cost)
        # Your implementation :)

    # TODO : Complete the search algorithms below!
    # You will need to complete the following search algorithms: BFS, DFS, UCS and AStar

    # Hints:
    # 1. Aside from the algorithms that you'll be evaluated on, we've included a function called "best_first_search"
    # Best first search is a general search method, that is optional to implement, however we would highly recommend it
    # You are free to use best_first_search in other search algorithms
    # 2. We've provided three types of Queues for you to use: Queue, LifoQueue and PriorityQueue. You do not need to
    # worry about implementing these data structures
    # 3. A rough template for each algorithm is as follows
    # - create a start node using the starting coordinates of the maze
    # - initialize an appropriate frontier
    # - expand nodes and add to the frontier as needed
    # - goal test as needed
    # 4. You might need a way to keep track of where you've already been

    """
    Implement the generic best-first-search algorithm here. 

    Inputs: 
    1. A start node
    2. A frontier (i.e, a queue)

    Return a tuple of three items:
    1. A boolean indicating whether or not the goal is reachable from the start
    2. The path from the start of the maze to the end of the maze. If no path exists, return None 
       (Hint: see the trace_back function in the node class)    
    3. The list of expanded nodes
    """

    def best_first_search(self, start_node, frontier):
        self.clear_expansion_history()
        # TODO : Your Implementation :)

    """
    Implement breadth-first-search here
    Return a tuple of three items:
    1. A boolean indicating whether or not the goal is reachable from the start
    2. The path from the start of the maze to the end of the maze. If no path exists, return None
        (Hint: see the trace_back function in the node class)
    3. The list of expanded nodes
    """

    def bfs(self):
        self.clear_expansion_history()
        # TODO : Your Implementation goes below

    """
    Implement depth-first-search here
    Return a tuple of three items:
    1. A boolean indicating whether or not the goal is reachable from the start
    2. The path from the start of the maze to the end of the maze. If no path exists, return None
       (Hint: see the trace_back function in the node class)
    3. The list of expanded nodes
    """

    def dfs(self):
        self.clear_expansion_history()
        # TODO : Your Implementation :)

    """
    Implement uniform-cost-search here
    Return a tuple of three items:
    1. A boolean indicating whether or not the goal is reachable from the start
    2. The path from the start of the maze to the end of the maze. If no path exists, return None
       (Hint: see the trace_back function in the node class)
    3. The list of expanded nodes
    """

    def ucs(self):
        self.clear_expansion_history()
        # TODO: Your Implementation :)

    """
    Implement A* search here
    Return a tuple of three items:
    1. A boolean indicating whether or not the goal is reachable from the start
    2. The path from the start of the maze to the end of the maze. If no path exists, return None
        (Hint: see the trace_back function in the node class)
    3. The list of expanded nodes
    """

    def astar(self):
        self.clear_expansion_history()
        # TODO : Your Implementation :)
