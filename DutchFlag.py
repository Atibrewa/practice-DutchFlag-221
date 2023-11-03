import random

def DutchFlag(A):
    #A is the array of length n we are sorting
    LastLow = -1
    FirstHigh = len(A)
    mid = 0
    ECount, SCount = 0, 0
    while mid < FirstHigh:
        if Examine(A, mid) == "r":
            LastLow += 1
            Swap(A,LastLow,mid)
            mid += 1
            ECount += 1
            SCount += 1
        elif Examine(A,mid) == "w":
            mid += 1
            ECount += 1
        elif Examine(A, mid) == "b":
            FirstHigh -= 1
            Swap(A,mid,FirstHigh)
            ECount += 1
            SCount += 1
        else:
            print("invalid element in given array")
            break
    print ("ECount :", ECount, ", SCount :", SCount)
    return A


def Examine(A,i):
    return A[i]
    
def Swap(A,i,j):
    A[i], A[j] = A[j], A[i]


# Testing and Running!
DutchFlag(['b','b','r','w','r','w']) # basic test
DutchFlag(['r','r','r','r','r','r']) # all red
DutchFlag(['w','w','w','w','w','w']) # all white
DutchFlag(['b', 'b', 'b', 'b', 'b']) # all blues
DutchFlag(['r','r','w','w','b','b']) # in order
DutchFlag(['w','w','b','b','b','b']) # no red, w and b are in order
DutchFlag(['r','r','b','b','b','b']) # no white
DutchFlag(['r','r','b','b','M','b']) #catch unexpected values

# generating random lists on order of thousands
list = ["r", "w", "b"]
ten = random.choices(list, weights=[1, 1, 1], k=10000)
twenty = random.choices(list, weights=[1, 1, 1], k=20000)
thirty = random.choices(list, weights=[1, 1, 1], k=30000)
forty = random.choices(list, weights=[1, 1, 1], k=40000)
fifty = random.choices(list, weights=[1, 1, 1], k=50000)

DutchFlag(ten)
DutchFlag(twenty)
DutchFlag(thirty)
DutchFlag(forty)
DutchFlag(fifty)
