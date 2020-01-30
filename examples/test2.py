import numpy as np
import json
import sys
config = json.load(open("config.json"))
projPath = config["projPath"]
sys.path.append(projPath)
from algorithm.simulator import *
from algorithm.reactionParameter import *

def main():
    myPara = Parameters()
    myPara.rho1 = 6
    myPara.rho2 = 2.5
    myPara.phi = 10
    myPara.theta = 1
    myPara.gamma1 = 0.004
    myPara.gamma2 = 0.25
    myPara.sigma1 = 10
    myPara.sigma2 = 1
    myPara.epsln1 = 1
    myPara.epsln2 = 0.1
    myPara.epsln3 = 1

    N=1000
    t_max = 20.


    myCell = Cell(4, myPara.init_ss, 3, myPara.reactantNuclear, myPara.productNuclear,
            myPara.reactionRateNuclear(), myPara.reactantCytoplasm, myPara.productCytoplasm,
            myPara.reactionRateCytoplasm(), myPara.spreadRateNC(), myPara.spreadRateCN(),
            myPara.spreadRateCC())

    data = []
    for i in range(N):
        df = myCell.simulate(t_max+1)
        s = df[df.index>t_max]["D"].mean()
        data.append(s)
        print("simulation", i, ":", s)

    plt.hist(data, bins=np.linspace(0,160,21), density=1)
    plt.show()

if __name__ == "__main__":
    main()