import numpy as np
paramsDict = {
    "init_ss": np.array([1,0,0,0]),
    "spreadRateNC": np.array([0,0,1,1]), ## [x,x,sigma1,epsilon1]
    "spreadRateCC": np.array([0,0,1,1]), ## [x,x,sigma2,epsilon3]
    "spreadRateCN": np.array([0,0,0,1]), ## [x,x,x,epsilon2]
    "reactionRateNuclear": np.array([1,1,1,1]), ## [gamma1, gamma2, rho1, rho2]
    "reactionRateCytoplasm": np.array([1,1,1]), ## [phi, theta, 1]
    "reactantNuclear": np.array([
        [1,0,0,1],
        [0,1,0,0],
        [1,0,0,0],
        [0,1,0,0]
    ]),
    "productNuclear": np.array([
        [0,1,0,0],
        [1,0,0,1],
        [1,0,1,0],
        [0,1,1,0]
    ]),
    "reactantCytoplasm": np.array([
        [0,0,1,0],
        [0,0,0,1],
        [0,0,1,0]
    ]),
    "productCytoplasm": np.array([
        [0,0,0,1],
        [0,0,0,1],
        [0,0,1,0]
    ])
}
class Parameters:
    def __init__(self):
        self.init_ss = np.array([1,0,0,0])

        self.gamma1 = 1; self.gamma2 = 1
        self.rho1 = 1; self.rho2 = 1
        self.theta = 1; self.phi = 1
        self.sigma1 = 1; self.sigma2 = 1
        self.epsln1 = 1; self.epsln2 = 0; self.epsln3 = 1

        self.reactantNuclear = np.array([
            [1,0,0,1],
            [0,1,0,0],
            [1,0,0,0],
            [0,1,0,0]
        ])
        self.productNuclear = np.array([
            [0,1,0,0],
            [1,0,0,1],
            [1,0,1,0],
            [0,1,1,0]
        ])
        self.reactantCytoplasm = np.array([
            [0,0,1,0],
            [0,0,0,1],
            [0,0,1,0]
        ])
        self.productNuclear = np.array([
            [0,0,0,1],
            [0,0,0,1],
            [0,0,1,0]
        ])

        def spreadRateNC(self):
            return np.array([0,0,self.sigma1,self.epsln2])

        def spreadRateCN(self):
            return np.array([0,0,0,self.epsln2])

        def spreadRateCC(self):
            return np.array([0,0,self.sigma2,self.epsln3])

        def reactionRateNuclear(self):
            return np.array([self.gamma1, self.gamma2, self.rho1, self.rho2])

        def reactionRateCytoplasm(self):
            return np.array([self.phi, self.theta, 1])
