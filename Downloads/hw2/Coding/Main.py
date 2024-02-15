from Engine import ChessEngine
from Evaluator import SimplifiedEvaluator
from Agent import Agent
import time

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
    print("Running tests in bulk and generating results file.....")
    testPath = "./Tests/test_FENs.txt"
    resultPath = "./Tests/results.txt"
    runTestAndWriteResults(testPath, resultPath, engine)

