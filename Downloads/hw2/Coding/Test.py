'''
To test in bulk, use Main.py and compare your answer to the expected_results.txt file

Please note - this file will let you check if your agent is producing the right move sequence, but it will not
validate if it is fast enough. Once your individual test cases pass, use Main.py to get a file that will
give you an idea of how fast your algorithm is running.

'''

from Engine import ChessEngine
from Evaluator import SimplifiedEvaluator
from Agent import Agent
import time
import sys

def trimNewline(s):
    if s[-1] == '\n':
        return s[:len(s)-1]
    return s

# This runs an agent for a specific input and times the execution
def runAgent(fen, engine, maxPly):
    startBoard = engine.createBoardFromFen(fen)
    evaluator = SimplifiedEvaluator(startBoard.turn)
    agent = Agent(fen, maxPly, engine, evaluator)
    start = time.time()
    moveSequence = agent.getMinimaxMoveSequence()
    end = time.time()
    return {"moves":moveSequence, "time":end-start}

# A simple function to parse the test file
def readTestFile(testPath):
    with open(testPath, 'r') as f:
        lines = f.readlines()
    testcases = []
    for line in lines:
        ply, fen = line.split('\t')
        testcases.append((ply, fen))
    return testcases

def readExpectedResults(groundtruthPath):
    with open(groundtruthPath, 'r') as f:
        lines = f.readlines()
    testcases = []
    for line in lines:
        ply, fen, expectedMoves = line.split('\t')
        testcases.append((ply, fen, str(expectedMoves)))
    return testcases

def runTestAndWriteResults(testPath, resultPath, engine):
    testcases = readTestFile(testPath)
    testcounter = 0
    with open(resultPath, 'w') as f:
        for test in testcases:
            testcounter +=1
            print("Running test "+str(testcounter)+".....")
            ply = int(test[0])
            fen = trimNewline(test[1])
            result = runAgent(fen, engine, ply)
            f.write("FEN:" + fen + '\n')
            f.write("PLY:" + str(ply) + '\n')
            f.write("MOVES:" + str(result['moves']) + '\n')
            f.write("TIME:" + str(result['time']) + '\n')
            f.write("##############\n")
    print("Tests complete")

if __name__ == '__main__':
    engine = ChessEngine()
    expectedResults = readExpectedResults("./Tests/expected_moves.txt")
    testCases = readTestFile("./Tests/test_FENs.txt")
    testNumber = int(sys.argv[1])
    print("Running move sequence test for test case ", testNumber)
    if (testNumber < 1) or (testNumber > 4):
        print("Invalid test number. Valid test numbers are 1,2,3, and 4")
    test = testCases[testNumber-1]
    expected = expectedResults[testNumber-1]
    ply = int(test[0])
    fen = trimNewline(test[1])
    result = runAgent(fen, engine, ply)
    expectedSequence = trimNewline(expected[2])
    if (str(result['moves']) !=  expectedSequence):
        print("Move Sequence Test ", testNumber, " FAILED")
        print("Predicted move sequence:",  str(result['moves']))
        print("Expected move sequence:", expectedSequence)
    else:
        print("Move Sequence Test ", testNumber, " Passed")


