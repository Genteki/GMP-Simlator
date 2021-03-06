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


    myCell = Cell(4, myPara.init_ss, 3, myPara.reactantNuclear, myPara.productNuclear,
            myPara.reactionRateNuclear(), myPara.reactantCytoplasm, myPara.productCytoplasm,
            myPara.reactionRateCytoplasm(), myPara.spreadRateNC(), myPara.spreadRateCN(),
            myPara.spreadRateCC())
    df = myCell.simulate(200)
    plt.plot(df.index, df["D"])
    plt.show()
    df.to_csv(projPath+"/output/test1.csv")

if __name__ == "__main__":
    main()
