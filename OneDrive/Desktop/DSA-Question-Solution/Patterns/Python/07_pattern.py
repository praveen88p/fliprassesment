#link = https://www.naukri.com/code360/problems/star-triangle_6573671?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SOLUTION

#Approach -1 
def nStarTriangle(n: int) -> None:
    for row in range(n):
        
        for col in range(n-1-row):
            print(" ",end="")

        for col in range(2*row+1):
            print("*",end="")

        # for col in range(n-1-row):
        #     print(" ",end="")
        print()
    pass

##########################################################################
#Approach -2

def nStarTriangle(n: int) -> None:

    # Initialise 'gap' and 'stars'.
    gap = n - 1
    stars = 1
    for i in range(n):
        for j in range(gap):
            print(' ', end="")
        for j in range(gap, gap+stars):
            print('*', end="")

        # End the current row of the pattern.
        print()

        gap -= 1
        stars += 2