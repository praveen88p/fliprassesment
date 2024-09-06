# Link = https://www.naukri.com/code360/problems/reverse-star-triangle_6573685?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION

def nStarTriangle(n: int) -> None:
    for row in range(n):
        
        for col in range(row):
            print(" ",end="")

        for col in range(2*(n-1-row)+1):
            print("*",end="")

        # for col in range(n+1+row):
        #     print(" ",end="")

        print()
    pass