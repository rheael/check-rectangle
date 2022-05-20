import re

class SetOfPoints:
    def __init__(self, points):
        self.points = points
    def IsYEqual(self):
        '''
        Function to look if there are exactly two couple of points with equal Y value.
        '''
        # Initialize equal with false and the points with equal Y value with empty array
        foundEqual = False
        YEqualPoints = []
        # Compare the points and find if there are equal Y value
        for i in range (4):
            for j in range (i+1,4):
                if(i+1<4):
                    # Found a couple of points with equal Y value
                    if(points[i][1]==points[j][1]):
                        if(foundEqual==False):
                            # Mark that one couple with equal Y value has been found
                            foundEqual = True
                            # Add to the matrix
                            YEqualPoints = [[points[i], points[j]]]
                            # Store the Y value to check for the next iteration
                            YEqual = points[i][1]
                        else: 
                            if(points[i][1]==YEqual): # There are more than 2 points with the same Y value
                                break
                            else: # The couple of points have different Y value, add to the matrix
                                YEqualPoints.append([points[i], points[j]])
        if(len(YEqualPoints)==2): # There are exactly two couple of points with equal Y value
            return (YEqualPoints)
    def IsXEqual(self, YEqualPoints):
        '''
        Function to look if there are exactly two couple of points with equal X value.
        '''
        # Initialize equal with false and the points with equal X value with empty array
        XEqualPoints = []
        # Compare the points and find if there are equal X value
        for i in range (2):
            for j in range (i+1):
                if(i+1<3):
                    # Found a couple of points with equal X value
                    if(YEqualPoints[0][i][0]==YEqualPoints[1][j][0]):
                        # Add to the matrix
                        XEqualPoints = [[YEqualPoints[0][i],YEqualPoints[1][j]]]
                        # Swap the index and check if the other couple has equal X value as well
                        i = SwapZeroAndOne(i)
                        j = SwapZeroAndOne(j)      
                        if(YEqualPoints[0][i][0]==YEqualPoints[1][j][0]):
                            # Store the X value to check for the next iteration
                            XEqualPoints.append([YEqualPoints[0][i],YEqualPoints[1][j]])
        if(len(XEqualPoints)==2): # There are exactly two couple of points with equal Y value
            return (XEqualPoints)
    def distanceArray(self,YEqualPoints,XEqualPoints):
        '''
        Returns distance array filled with 
        Does not use euclidean distance due to having equal X points and Y points,
        so the distance equals to substraction on the other axis.
        '''
        distance = []
        for i in range (2):
            dist = YEqualPoints[i][0][0] - YEqualPoints[i][1][0]
            distance.append(dist)
            dist = XEqualPoints[i][0][1] - XEqualPoints[i][1][1]
            distance.append(dist)
        return distance

def SwapZeroAndOne(x):
    '''
    Swap x value from 0 to 1 or 1 to 0.
    '''
    if(x==0):
        return 1
    if(x==1):
        return 0  
def isSquare(distance):
    '''
    Check if the rectangle is square, all sides are equal.
    '''
    if(distance[0]==distance[1]==distance[2]==distance[3]):
        return True
    else:
        return False
def isSamePointExist(distance):
    '''
    Check if there exists two same points.
    '''
    if(distance[0]==0 or distance[1]==0 or distance[2]==0 or distance[3]==0):
        return True
    else:
        return False

userInputFormat = False
# Read input from user 
while(userInputFormat==False):
    userInput = input("Masukkan set dengan format ((x1,y1),(x2,y2),(x3,y3),(x4,y4))\n")
    # Check the format of user input with regex
    userInput = re.findall("(\d,\d)",userInput)
    if(len(userInput)==4):
        # Correct format
        userInputFormat = True
        # Initialize points
        points = [[0 for i in range (0)] for j in range (4)]
        for i in range (4):
            for j in range (2):
                # Process the input to append to points array
                points[i].append(int(userInput[i].split(",")[j]))
        # Create an object of points
        setOfPoints = SetOfPoints(points)
        YEqualPoints = setOfPoints.IsYEqual()
        if(YEqualPoints!=None): # Equal Y value found
            XEqualPoints = setOfPoints.IsXEqual(YEqualPoints)
            if(XEqualPoints!=None): # Equal X value found
                distance = setOfPoints.distanceArray(YEqualPoints,XEqualPoints)
                if(isSquare(distance)): # The rectangle is square
                    print("Masukan bukan persegi panjang.")
                else:
                    if(isSamePointExist(distance)): # Same point exists
                        print("Masukan bukan persegi panjang.")
                    else:
                        print("Masukkan berupa persegi panjang.")
            else:
                print("Masukan bukan persegi panjang.")
        else:
            print("Masukan bukan persegi panjang.")
    else:
        print("Format masukan salah.")