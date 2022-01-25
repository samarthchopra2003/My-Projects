import numpy as np
import random
from matplotlib import pyplot as plt
import math

#river lattice
xi=0 #x initial position=0
yi=0 #y initial position=0

matrixsize=[10,20,30]

for n in matrixsize:

    problist=[] #resetting problist

    for k in range(0,100): #changing probability from 0 to 10
        success=0
        avgsuccess=0
        for t in range(100):

            x=np.zeros((n,n)) #Creating array
            x[xi][yi]=1 #initial position should have a rock

            count=0 #tracks no. of rocks used

            for i in range(n):
                for j in range(n):
                    p=random.randrange(0,100) #control variable
                    if p<=k: #determines probability of matrix composed of stones
                        x[i][j]=1.1
                        count+=1

            #start of cluster and union algorithm
            clusternum=1

            #clustering loop
            for i in range(n):
                for j in range(n):
                    if i==0 and j==0: #left upper corner case
                        x[i][j]=clusternum
                        continue
                    else:
                        pass
                    if x[i][j]!=0:
                        if i==0 and j!=(n-1): #top line middle case
                            if x[i][j-1]!=1.1 and x[i][j-1]!=0:
                                x[i][j]=x[i][j-1]
                            elif x[i][j+1]!=1.1 and x[i][j-1]!=0: #no need to check for bottom cell as it has not been assigned cluster value yet
                                x[i][j]=x[i][j+1]
                            else:
                                clusternum+=1
                                x[i][j]=clusternum
                        elif j==(n-1) and i==0: #right upper corner case
                            if x[i][j-1]!=1.1 and x[i][j-1]!=0: #just check cell before as bottom cell has not been assigned cluster value
                                x[i][j]=x[i][j-1]
                            else:
                                clusternum+=1
                                x[i][j]=clusternum
                        elif j==(n-1) and i!=0 and i!=(n-1): #right side middle case
                            if x[i][j-1]!=1.1 and x[i][j-1]!=0:
                                x[i][j]=x[i][j-1]
                            elif x[i-1][j]!=1.1 and x[i-1][j]!=0:
                                x[i][j]=x[i-1][j]
                            else:
                                clusternum+=1
                                x[i][j]=clusternum
                        elif j==0 and i!=0 and i!=(n-1): #left side middle case
                            if x[i-1][j]!=1.1 and x[i-1][j]!=0: #no need to check right cell as it has not been checked yet
                                x[i][j]=x[i-1][j]
                            else:
                                clusternum+=1
                                x[i][j]=clusternum
                        elif j==0 and i==(n-1): #left bottom corner case
                            if x[i-1][j]!=1.1 and x[i-1][j]!=0: #only upper cell needs to be checked
                                x[i][j]=x[i-1][j]
                            else:
                                clusternum+=1
                                x[i][j]=clusternum
                        elif i==(n-1) and j!=0 and j!=n-1: #bottom line case
                            if x[i][j-1]!=1.1 and x[i][j-1]!=0: 
                                x[i][j]=x[i][j-1]
                            elif x[i-1][j]!=1.1 and x[i-1][j]!=0:
                                x[i][j]=x[i-1][j]
                            else:
                                clusternum+=1
                                x[i][j]=clusternum
                        elif i==(n-1) and j==(n-1): #right bottom corner case
                            if x[i][j-1]!=1.1 and x[i][j-1]!=0: 
                                x[i][j]=x[i][j-1]
                            elif x[i-1][j]!=1.1 and x[i-1][j]!=0:
                                x[i][j]=x[i-1][j]
                            else:
                                clusternum+=1
                                x[i][j]=clusternum
                        else: #all other cases
                            if x[i][j-1]!=1.1 and x[i][j-1]!=0: #cell to the left
                                x[i][j]=x[i][j-1]
                            elif x[i-1][j]!=1.1 and x[i-1][j]!=0: #cell above
                                x[i][j]=x[i-1][j]
                            elif x[i+1][j]!=1.1 and x[i+1][j]!=0: #cell below
                                x[i][j]=x[i+1][j]
                            elif x[i][j+1]!=1.1 and x[i][j+1]!=0: #cell to the right
                                x[i][j]=x[i][j+1]
                            else:
                                clusternum+=1
                                x[i][j]=clusternum

            #union algorithm
            for m in range(math.ceil(0.0208*n**3+0.125*n**2+1.6667*n-5)): #range needs to be changed based on matrix size
                for i in range(n):
                    for j in range(n):
                        if i==0 and j==0: #left upper corner case
                            if x[i][j]!=x[i][j+1] and x[i][j+1]!=0 and x[i][j]!=0: #cell to the right
                                if x[i][j]<x[i][j+1]:
                                    x[i][j+1]=x[i][j]
                                else:
                                    x[i][j]=x[i][j+1]
                        elif i==0 and j!=(n-1) and j!=0: #top line middle case
                            if x[i][j]!=x[i+1][j] and x[i+1][j]!=0 and x[i][j]!=0: #cell to the bottom
                                if x[i][j]<x[i+1][j]:
                                    x[i+1][j]=x[i][j]
                                else:
                                    x[i][j]=x[i+1][j]
                            if x[i][j]!=x[i][j+1] and x[i][j+1]!=0 and x[i][j]!=0: #cell to the right
                                if x[i][j]<x[i][j+1]:
                                        x[i][j+1]=x[i][j]
                                else:
                                    x[i][j]=x[i][j+1]
                            if x[i][j]!=x[i][j-1] and x[i][j-1]!=0 and x[i][j]!=0: #cell to the left
                                if x[i][j]<x[i][j-1]:
                                    x[i][j-1]=x[i][j]
                                else:
                                    x[i][j]=x[i][j-1]
                        elif j==(n-1) and i==0: #right upper corner case
                            if x[i][j]!=x[i][j-1] and x[i][j-1]!=0 and x[i][j]!=0: #cell to the left
                                if x[i][j]<x[i][j-1]:
                                    x[i][j-1]=x[i][j]
                                else:
                                    x[i][j]=x[i][j-1]
                            if x[i][j]!=x[i+1][j] and x[i+1][j]!=0 and x[i][j]!=0: #cell to the bottom
                                if x[i][j]<x[i+1][j]:
                                    x[i+1][j]=x[i][j]
                                else:
                                    x[i][j]=x[i+1][j]
                        elif j==(n-1) and i!=0 and i!=n-1: #right side middle case
                            if x[i][j]!=x[i-1][j] and x[i-1][j]!=0 and x[i][j]!=0: #cell above
                                if x[i-1][j]<x[i][j]:
                                    x[i-1][j]=x[i][j]
                                else:
                                    x[i][j]=x[i-1][j]
                            if x[i][j]!=x[i+1][j] and x[i+1][j]!=0 and x[i][j]!=0: #cell to the bottom
                                if x[i][j]<x[i+1][j]:
                                    x[i+1][j]=x[i][j]
                                else:
                                    x[i][j]=x[i+1][j]
                            if x[i][j]!=x[i][j-1] and x[i][j-1]!=0 and x[i][j]!=0: #cell to the left
                                if x[i][j]<x[i][j-1]:
                                    x[i][j-1]=x[i][j]
                                else:
                                    x[i][j]=x[i][j-1]
                        elif j==0 and i!=0 and i!=(n-1): #left side middle case
                            if x[i][j]!=x[i-1][j] and x[i-1][j]!=0 and x[i][j]!=0: #cell above
                                if x[i-1][j]<x[i][j]:
                                        x[i-1][j]=x[i][j]
                                else:
                                    x[i][j]=x[i-1][j]
                            if x[i][j]!=x[i+1][j] and x[i+1][j]!=0 and x[i][j]!=0: #cell to the bottom
                                if x[i][j]<x[i+1][j]:
                                    x[i+1][j]=x[i][j]
                                else:
                                    x[i][j]=x[i+1][j]
                            if x[i][j]!=x[i][j+1] and x[i][j+1]!=0 and x[i][j]!=0: #cell to the right
                                if x[i][j]<x[i][j+1]:
                                    x[i][j+1]=x[i][j]
                                else:
                                    x[i][j]=x[i][j+1]
                        elif j==0 and i==(n-1): #left bottom corner case
                            if x[i][j]!=x[i-1][j] and x[i-1][j]!=0 and x[i][j]!=0: #cell above
                                if x[i-1][j]<x[i][j]:
                                    x[i-1][j]=x[i][j]
                                else:
                                    x[i][j]=x[i-1][j]
                            if x[i][j]!=x[i][j+1] and x[i][j+1]!=0 and x[i][j]!=0: #cell to the right
                                if x[i][j]<x[i][j+1]:
                                    x[i][j+1]=x[i][j]
                                else:
                                    x[i][j]=x[i][j+1]
                        elif i==(n-1) and j!=0 and j!=n-1: #bottom line case
                            if x[i][j]!=x[i-1][j] and x[i-1][j]!=0 and x[i][j]!=0: #cell above
                                if x[i-1][j]<x[i][j]:
                                    x[i-1][j]=x[i][j]
                                else:
                                    x[i][j]=x[i-1][j]
                            if x[i][j]!=x[i][j-1] and x[i][j-1]!=0 and x[i][j]!=0: #cell to the left
                                if x[i][j]<x[i][j-1]:
                                    x[i][j-1]=x[i][j]
                                else:
                                    x[i][j]=x[i][j-1]
                            if x[i][j]!=x[i][j+1] and x[i][j+1]!=0 and x[i][j]!=0: #cell to the right
                                if x[i][j]<x[i][j+1]:
                                    x[i][j+1]=x[i][j]
                                else:
                                    x[i][j]=x[i][j+1]
                        elif i==(n-1) and j==(n-1): #right bottom corner case
                            if x[i][j]!=x[i-1][j] and x[i-1][j]!=0 and x[i][j]!=0: #cell above
                                if x[i-1][j]<x[i][j]:
                                    x[i-1][j]=x[i][j]
                                else:
                                    x[i][j]=x[i-1][j]
                            if x[i][j]!=x[i][j-1] and x[i][j-1]!=0 and x[i][j]!=0: #cell to the left
                                if x[i][j]<x[i][j-1]:
                                    x[i][j-1]=x[i][j]
                                else:
                                    x[i][j]=x[i][j-1]
                        else: #all other cases
                            if x[i][j]!=x[i-1][j] and x[i-1][j]!=0 and x[i][j]!=0: #cell above
                                if x[i-1][j]<x[i][j]:
                                    x[i-1][j]=x[i][j]
                                else:
                                    x[i][j]=x[i-1][j]
                            if x[i][j]!=x[i][j-1] and x[i][j-1]!=0 and x[i][j]!=0: #cell to the left
                                if x[i][j]<x[i][j-1]:
                                    x[i][j-1]=x[i][j]
                                else:
                                    x[i][j]=x[i][j-1]
                            if x[i][j]!=x[i][j+1] and x[i][j+1]!=0 and x[i][j]!=0: #cell to the right
                                if x[i][j]<x[i][j+1]:
                                    x[i][j+1]=x[i][j]
                                else:
                                    x[i][j]=x[i][j+1]
                            if x[i][j]!=x[i+1][j] and x[i+1][j]!=0 and x[i][j]!=0: #cell to the bottom
                                if x[i][j]<x[i+1][j]:
                                    x[i+1][j]=x[i][j]
                                else:
                                    x[i][j]=x[i+1][j]

            #path across from top to bottom
            for i in range(1,clusternum+1):
                for j in range(n):
                    if x[0][j]==i and x[n-1][j]==i:
                        success+=1
                        break
                    if x[j][0]==i and x[j][n-1]==i:
                        success+=1
                        break
        problist.append((k,success))

    x_val = []
    y_val = []
    for i in range(len(problist)):
        x_val.append(problist[i][0])
        y_val.append(problist[i][1])

    plt.plot(x_val,y_val)

plt.legend(['10x10 matrix','20x20 matrix','30x30 matrix'])
plt.xlabel('Probability')
plt.ylabel('Success rate (0-100)')
plt.title('Lattice Problem')
plt.show()

print(problist)


