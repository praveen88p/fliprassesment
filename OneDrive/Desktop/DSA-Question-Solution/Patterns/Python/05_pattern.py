#link = https://www.naukri.com/code360/problems/seeding_6581892?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def seeding(n: int) -> None:
    for row in range(n):
        for col in range(n):
            print("*",end=" ")
        n-=1
        print()
    pass