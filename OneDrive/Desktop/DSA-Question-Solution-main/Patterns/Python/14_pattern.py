# Link = https://www.naukri.com/code360/problems/number-crown_6581894?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION

n=5


for row in range(n):
    for col in range(row +1):
            print(col+1,end = "")
        
    for col in range((n-row-1)*2):
            print(" ",end="")
        
    for col in range(row+1,0,-1):
            print(col,end ="")

    print()
