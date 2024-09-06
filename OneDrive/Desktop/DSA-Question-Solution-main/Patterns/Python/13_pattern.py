#Link = https://www.naukri.com/code360/problems/increasing-number-triangle_6581893?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION

def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    k=1
    for row in range(n):
        for col in range(row+1):
            print(k,end=" ")
            k+=1
        print()

    pass
