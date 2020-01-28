import json 
import sys
import numpy as np
config = json.load(open("config.json"))
projPath = config["projPath"]
sys.path.append(projPath)
from algorithm.simulator import *

init_ss = np.array([1,0,0,0])
ncSpreadRate = np.array([0,0,1,1])
ccSpreadRate = np.array([0,0,1,1])
cnSpreadRate = np.array([0,0,0,0])
reactionRateNuclear = np.array([1,1,1,1])
reactionRateCytoplasm = np.array([1,1,1])
reactantNuclear = np.array([
    [1,0,0,1],
    [0,1,0,0],
    [1,0,0,0],
    [0,1,0,0]
])
productNuclear = np.array([
    [0,1,0,0],
    [1,0,0,1],
    [1,0,1,0],
    [0,1,1,0]
])
reactantCytoplasm = np.array([
    [0,0,1,0],
    [0,0,0,1],
    [0,0,1,0]
])
productCytoplasm = np.array([
    [0,0,0,1],
    [0,0,0,1],
    [0,0,1,0]
])

cell = Cell(4,init_ss,2,reactantNuclear,productNuclear,reactionRateNuclear
,reactantCytoplasm,productCytoplasm,reactionRateCytoplasm,
ncSpreadRate,cnSpreadRate,ccSpreadRate)

if __name__ == "__main__":
    cell.simulate(10)