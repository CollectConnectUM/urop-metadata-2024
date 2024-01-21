"""
The test runner - use this to check if your implementation seems sound
This test runner does NOT automatically evaluate your implementation, it just visualizes it
"""
from Maze import Maze
from Agent import Agent
import sys


# Load a test maze and create the agent
def load_agent(test_number):
    testfile = "./Tests/Test"+test_number+".test"
    test_maze = Maze(testfile)
    agent = Agent(test_maze)
    return agent


def print_result(test_number, algo, result):
    print("Results for", algo, "for test case", str(test_number))
    print("Path found:", result[0])
    print("Final path:", result[1][0])
    print("Action Sequence:", result[1][1])
    print("Expansion history:", result[2])


def run_test(test_number, algo=None):
    test_agent = load_agent(test_number)
    algo = algo.upper()
    if algo == "BFS":
        result = test_agent.bfs()
    elif algo == "DFS":
        result = test_agent.dfs()
    elif algo == "UCS":
        result = test_agent.ucs()
    elif algo == "ASTAR":
        result = test_agent.astar()
    else:
        result = None
    if result is not None:
        print_result(test_number, algo, result)
        test_agent.visualize_expansion(result[1][0])


# Use this block of code to run the test via a command line
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid number of arguments!\n Expected usage: python LocalTest.py TESTNUMBER TESTALGO\n"
              "For example: python LocalTest.py 0 BFS")
    else:
        test_number = sys.argv[1]
        test_algo = sys.argv[2]
        run_test(test_number, test_algo)

# If you would rather run this test from an IDE instead of the command line, feel free to comment out the If block
# You can simply call the run_test function directly. For example:
# run_test('0', 'BFS')
