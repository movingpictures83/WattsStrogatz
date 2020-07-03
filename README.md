# WattsStrogatz
# Language: Python
# Input: TXT
# Output: GML
# Tested with: PluMA 1.1, Python 3.6
# Dependency: networkx==2.2

PluMA plugin that uses the Watts-Strogatz algorithm (Watts and Strogatz, 1998) to compute a random network of a user-specified number of nodes, the number of nearest neighbors (note: uses a ring topology) and a probability for rewiring each edges.

These values are supplied in an input TXT file of tab-delineated keywords and values ("nodes", "k", and "probability" respectively).

Output will be the network, in the Graph Modeling Language (GML) format.
