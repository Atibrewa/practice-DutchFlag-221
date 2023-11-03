# homework-4-aaaaaaaaaaa
homework-4-aaaaaaaaaaa created by GitHub Classroom

Algorithm for the Dutch Flag Problem!

Algorithm DutchFlag(A)
// A is the array of length n we are sorting
LastLow = -1
mid = 0
FirstHigh = n
until mid <= FirstHigh
    if examine(A,mid) == 'r':
        LastLow += 1
        swap(A,LastLow,mid)
        mid += 1
    else if examine(A,mid) == 'w':
        mid += 1
    else:
        FirstHigh -= 1
        swap(A,mid,FirstHigh)

For best case performance, with the least number of swaps, the greater the number of white the better performance (less # of swaps)
