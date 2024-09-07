# link = https://www.naukri.com/code360/problems/increasing-letter-triangle_6581897?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION


n=9

for row in range (n):
        for col in range(row+1):
            print(chr(col+65),end=" ")
        print()