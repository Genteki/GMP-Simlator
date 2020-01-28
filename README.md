
# GMP Simulator

It's a simulator program for DNA->mRNA->protein reactions system in cells

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
