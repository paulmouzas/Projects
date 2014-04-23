import math

def distance(p1,p2):
	return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
	
def closestPair(l):
	inf = float('inf')
	closest = inf
	points = None
	for i in range(len(l)):
		for j in range(i+1, len(l)):
			tmp = distance(l[i], l[j])
			if tmp < closest:
				closest = tmp
				points = (l[i], l[j])
	return closest, points
P =[(0,0),(7,6),(2,20),(12,5),(16,16),(5,8),(19,7),(14,22),(8,19),(7,29),(10,11),(1,13)]


print closestPair(P)