#link = https://www.naukri.com/code360/problems/n-2-forest_6570178?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
num=int(input())
def pattern(n):
    
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()
        

pattern(num)


