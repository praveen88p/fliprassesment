#link = https://www.naukri.com/code360/problems/triangle_6573690?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=PROBLEM
def triangle( n:int) ->None:
    for row in range(n):
        for col in range(row+1):
            print(row+1,end=" ")
        print()

    pass