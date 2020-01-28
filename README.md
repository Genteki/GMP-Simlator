
# GMP Simulator

It's a simulator program for DNA->mRNA->protein reactions system in cells

## Usage
### import
Directly import the package
> from algorithm.simulator import *

if you cannot import the package successfully, you should add you project path to sys.path:
> import sys  
sys.path.append("$your-project-path")
### initialize an example
> myCell = Cell(self, n, init_ss, layer,
nuclearReactant, nuclearProduct, nuclearRate,
cytoplasmReactant, cytoplasmProduct, cytoplsamRate,
ncSpread, cnSpread, ccSpread)

I've provide an example in *algorithm/simulatorTest.py* for the construction function.
### simulation
> myCell.simulate(maxTime)

## Reactions
### Nuclear
$$ G+P \rightleftharpoons G^*  $$
$$ G \to G + mRNA $$
$$ G^* \to G^* + mRNA $$
### Cytoplasm
$$ mRNA \to P $$
$$ P \to \varnothing $$
$$ mRNA \to \varnothing $$
### Spreading
$$ mRNA\left(\text{nuclear}\right) \to mRNA\left(\text{cytoplasm}\right)  $$
$$ P\left(\text{cytoplasm}\right) \rightleftharpoons P\left(\text{nuclear}\right) $$
$$ mRNA\left(\text{cytoplasm}\right) \rightleftharpoons mRNA\left(\text{cytoplasm}\right)  $$
$$ P\left(\text{cytoplasm}\right) \rightleftharpoons P\left(\text{cytoplasm}\right) $$

## Variables Definition
### state space
\[
    SS =
    \begin{bmatrix}
        G & G^* & mRNA & P
    \end{bmatrix} ^T
\]
### reaction matrix
\[
    R_{nuclear} =
    \begin{bmatrix}
        1 & 0 & 0 & 1 \\
        0 & 1 & 0 & 0 \\
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0    
    \end{bmatrix},
    P_{nuclear}  =
    \begin{bmatrix}
        0 & 1 & 0 & 0 \\
        1 & 0 & 0 & 1 \\
        1 & 0 & 1 & 0 \\
        0 & 1 & 1 & 0
    \end{bmatrix}
    \\
    R_{cytoplasm} =
    \begin{bmatrix}
        0 & 0 & 1 & 0 \\
        0 & 0 & 0 & 1 \\
        0 & 0 & 1 & 0
    \end{bmatrix},
    P_{cytoplasm} =
    \begin{bmatrix}
        0 & 0 & 0 & 1 \\
        0 & 0 & 0 & 0 \\
        0 & 0 & 0 & 0
    \end{bmatrix}
\]
