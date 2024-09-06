#Link = https://www.naukri.com/code360/problems/rotated-triangle_6573688?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SOLUTION

def nStarTriangle(n: int) -> None:
    # Write your code here.
    for row in range (n):
        for col in range(row+1):
            print("*",end="")
        print()

#for lower part
      
    for row in range(n-1):
        for col in range(n-1-row):
            print("*", end ="")
        
        print()
        

    pass

#approach 2
n=5
for row in range(2*n-1):
   
   if row<n:
        for col in range(row+1):
         print("*", end="")

   else:
      for col in range(2*n-1-row):
       print("*",end="")

   print()