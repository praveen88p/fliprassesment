#Link = https://www.naukri.com/code360/problems/reverse-number-triangle_6581889?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION


def nNumberTriangle(n: int) -> None:
    for row in range(n):
        for col in range(n):
            print(col+1, end = " ")
        n-=1
        print()
        
    pass