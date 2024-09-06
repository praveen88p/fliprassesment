# link = https://www.naukri.com/code360/problems/binary-number-triangle_6581890?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION
n = 5
for row in range (n):
    for col in range (row+1):
        
        if (row+col)%2 == 0:
            print("1",end = " ")
        else:
            print("0", end = " ")
        
    print()
