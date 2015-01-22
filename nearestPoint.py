import csv
import os
import sys
import math


#opens two files: each point from (1) will be compared, in turn, to all the points in (2)...
#(1) is x.csv, (2) is y.txt
#(1) is stored in structureList
#(2) is stored in compareList
#the result is written to a csv file ('x.csv')
def start():
    structureList = []
    with open('x.csv', 'r') as csvfile:
        structreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in structreader:
		    structureList.append(row)
			
	compareList = []
    with open('y.txt', 'r') as csvfile:
        structreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in structreader:
		    compareList.append(row)
	
    f = open('closestPoints.csv','wb')
    try:
        writer = csv.writer(f)
        writer.writerow(('x','y','z'))
        
        first = True
        for point in structureList:
            if first:
			    #ignore the first element (just the title)
                first = False
            else:
			    #see def compare(point, compareList)
                writer.writerow(compare(point,compareList))
    finally:
        f.close()	
	
#compares the single point to each point ('cpoint') in the compareList
#returns the closest point (from the compareList) in the form of a list (x,y,z)			
def compare(point,compareList):
    newpoint = point[0].split(',')
    x = newpoint[1]
    y = newpoint[2]
    distanceList = []
    
    for cpoint in compareList:
        newcpoint = cpoint[0].split(',')
        x2 = newcpoint[0]
        y2 = newcpoint[1]
        distanceList.append(distanceBetween(x, y, x2, y2))

    #finds the index of the closest point to the point passed into this (compare) method, searching the list of distances between that point and every other point
    closestPointIndex = distanceList.index(min(distanceList))
    closestPoint = compareList[closestPointIndex][0].split(',')	
	
    return closestPoint   
	
#distance formula
def distanceBetween(x, y, x2, y2):	
    x = float(x)
    y = float(y)
    x2 = float(x2)
    y2 = float(y2)
    return math.sqrt((x2 - x) * (x2 - x) + (y2 - y) * (y2 - y))

def main():
    start()
    
 
 
if __name__ == "__main__":
   main()
