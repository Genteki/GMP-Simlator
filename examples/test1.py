import numpy as np
import json
import sys
config = json.load(open("config.json"))
projPath = config["projPath"]
sys.path.append(projPath)
from algorithm.simulator import *
from algorithm.reactionParameter import *

gamma1 = 1; gamma2 = 1
rho1 = 1; rho2 = 1
theta = 1; phi = 1
sigma1 = 1; sigma2 = 1
epsln1 = 1; epsln2 = 0; epsln3 = 1
