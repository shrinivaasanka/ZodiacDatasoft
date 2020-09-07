import sys


def astar(distance,start,end,heuristic):
	discovered=[start]
	camefrom={}
	gscore={}
	fscore={}
	for n in range(len(distance[0])):
		gscore[n]=sys.maxsize
	gscore[start]=0
	for n in range(len(distance[0])):
		fscore[n]=sys.maxsize
	fscore[start]=heuristic[start]
	while len(discovered) > 0:
		print("discovered:",discovered)
		current=minimumscorenode(fscore,discovered)
		print("current:",current)
		if current==end:
			return print_astar_pathfound(camefrom,current)
		#if current in discovered:
		discovered.remove(current)
		for neigh in neighbours(current,distance):
			tentativegscore = gscore[current] + distance[current][neigh]
			print("tentativegscore:",tentativegscore)
			print("gscore:",gscore)
			print("fscore:",fscore)
			print("camefrom:",camefrom)
			if tentativegscore < gscore[neigh]:
				print("tentativegscore < gscore[neigh]")
				camefrom[neigh] = current
				gscore[neigh] = tentativegscore
				fscore[neigh] = gscore[neigh] + heuristic[neigh]
				if neigh not in discovered:
					discovered.append(neigh)

def minimumscorenode(scoremap,discovered):
	minscore=sys.maxsize
	minnode=-1
	for node,score in scoremap.items():
		if score < minscore and node in discovered:
			minscore = score
			minnode = node	
	print("minimumscorenode():minnode = ",minnode)
	return minnode	

def print_astar_pathfound(camefrom,current):
	pathfound = [current]
	while current in camefrom.keys():
		current = camefrom[current]
		pathfound.append(current)
	print("pathfound:",pathfound)
	return pathfound

def neighbours(node,distance):
	index=0
	nb=[]
	for adj in distance[node]:
		if adj > 0:
			nb.append(index)
		index+=1
	return nb

if __name__=="__main__":
	distance=[[0.01,0.0002,-1,0.34,0.45,0.56,0.4,0.002],
		[0.01,0.002,0.34,0.45,0.9,0.56,0.4,0.2],
		[0.01,0.0002,0.9,0.34,0.45,-1,0.4,0.002],
		[0.081,-1,0.94,0.9,-1,0.56,0.04,0.2],
		[0.01,0.002,0.54,0.47,-1,0.59,0.4,0.02],
		[0.01,0.2,0.34,-1,0.6,0.9,0.4,0.002],
		[0.01,0.002,-1,0.5,0.9,-1,0.4,0.02],
		[0.01,0.0002,-1,0.9,0.4,0.6,0.4,0.02]]
	heuristic={0:0.2,1:0.03,2:0.004,3:0.07,4:0.001,5:0.002,6:0.003,7:0.004}
	astar(distance,3,7,heuristic)
