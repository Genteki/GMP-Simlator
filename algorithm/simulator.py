import numpy as np
import matplotlib.pyplot as plt

class System:
    def __init__(self, n, init_ss, reactants=np.array([[]]), products=np.array([[]]),
    reaction_rate=np.array([]),next_spread_rate = None, prev_spread_rate=None, t=0):
        self.n = n
        self.ss = init_ss
        self.init_ss = init_ss
        self.reactants = reactants
        self.products = products
        self.reaction_rate = reaction_rate
        self.spread = np.diag([0]*n)
        if prev_spread_rate:
            self.prev_spread_rate = prev_spread_rate
        else:
            self.prev_spread_rate = np.zeros(n)
        if next_spread_rate:
            self.next_spread_rate = next_spread_rate
        else:
            self.next_spread_rate = np.zeros(n)
        self.time = t


    def getProspencities(self):
        # for chemstry reaction
        p1 = np.zeros(self.reactants.shape[0])
        prod = self.ss**self.reactants
        for i in range(self.reactants.shape[0]):
            p1[i] = np.products(prod)*self.reaction_rate
        # for spreading
        p2 = np.append(self.ss*self.next_spread_rate, self.ss*self.prev_spread_rate)
        # reaction, next, prev
        return np.append(p1,p2)

    def getDeltaT(self, p):
        return np.random.choice(range(self.reactants.shape[0]), p=p/p.sum())

    def determineReaction(self, p):
        r = self.reactants.shape[0]
        i = np.random.choice(range(r)+self.n*2, p=p/p.sum())
        if i < r:
            return (0, self.reactants[i], self.products[i])
        elif i < r+self.n:
            return (1, self.spread[i-r], self.spread[i-r])
        else:
            return (-1, self.spread[i-2*r], self.spread[i-2*r])

    def reset(self):
        self.ss = self.init_ss

class Cell:
    def __init__(self, n, init_ss, layer=3, 
    nuclearReactant=np.array([[]]), nuclearProduct=np.array([[]]), nuclearRate=np.array([]), 
    cytoplasmReactant=np.array([[]]), cytoplasmProduct=np.array([[]]), cytoplsamRate = np.array([]), 
    ncSpread=None, cnSpread=None, ccSpread=None):
        self.time = np.array([0]*layer)
        self.regions = []
        nuclear = System(n, init_ss, reactants=nuclearReactant, reaction_rate=nuclearRate,
        products=nuclearProduct, next_spread_rate=ncSpread)
        self.regions.append(nuclear)
        if n == 2:
            firstCytoplasm = System(n, np.zeros(n), reactants=cytoplasmReactant,
            products=cytoplasmProduct, reaction_rate=cytoplsamRate, prev_spread_rate=cnSpread,
            next_spread_rate=np.zeros(n))
            self.regions.append(firstCytoplasm)
            pass
        elif n >= 3:
            firstCytoplasm = System(n, np.zeros(n), reactants=cytoplasmReactant,
            products=cytoplasmProduct, reaction_rate=cytoplsamRate, prev_spread_rate=cnSpread,
            next_spread_rate=ccSpread)
            lastCytoplasm = System(n, np.zeros(n), reactants=cytoplasmReactant,
            products=cytoplasmProduct, reaction_rate=cytoplsamRate, prev_spread_rate=ccSpread,
            next_spread_rate=np.zeros(n))
            self.regions.append(firstCytoplasm)
            for i in range(2,n-1):
                newCytoplasm = System(n, np.zeros(n), reactants=cytoplasmReactant,
                products=cytoplasmProduct, reaction_rate=cytoplsamRate,
                prev_spread_rate=ccSpread, next_spread_rate=ccSpread)
                self.regions.append(newCytoplasm)
            self.regions.append(lastCytoplasm)
        

    def simulate(self, maxTime=10):
        while self.time.max() <= maxTime:
            i = np.argmin(self.time)
            p = self.regions[i].getProspencities()
            if (p==0).all():
                self.time[i]=self.time.max()
                continue
            else:
                dt = self.regions[i].getDeltaT(p)
                self.time[i]+=dt
                x, re, pr = self.regions[i].determineReaction(p)
                self.regions[i].ss-=re
                self.regions[i+x]+=pr

            print(self.time.max(), self.regions[0].ss)
        
        for region in self.regions:
            region.reset()
