import sys
import numpy as np
from collections import defaultdict

def hypervertices_intersections(hypergraph,intersectinghypervertices):
    hyperedges=hypergraph.values()
    intersections=set(hypergraph[intersectinghypervertices[0]])
    for ishv in intersectinghypervertices:
            v1 = hypergraph[ishv]
            setv1=set(v1)
            intersections=intersections.intersection(setv1)
    print('hypervertices intersection of ',intersectinghypervertices,':',intersections)

if __name__=="__main__":
    thoughtnet_hypergraph={'water':['flood caused by storms wrought havoc','water scarcity hits crops','cost effective sea water desalination would benefit agriculture'],'air':['flood caused by storms wrought havoc','air traffic flourished in last financial year','air pollution hits new high'],'agriculture':['water scarcity hits crops','cost effective sea water desalination would benefit agriculture']}
    thoughtnetevocations=hypervertices_intersections(thoughtnet_hypergraph,['water','air'])
    thoughtnetevocations=hypervertices_intersections(thoughtnet_hypergraph,['water','agriculture'])
    thoughtnetevocations=hypervertices_intersections(thoughtnet_hypergraph,['water','air','agriculture'])
