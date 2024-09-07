def nStarDiamond(n: int) -> None:
    
    for row in range(n):
        for col in range(n-1-row):
            print(" ",end="")

        for col in range(2*row+1):
            print("*", end = "")
        
        print()
        
    
    for row in range(n):
        
        for col in range(row):
            print(" ",end="")

        for col in range(2*(n-1-row)+1):
            print("*",end="")

       

        print() 

    pass