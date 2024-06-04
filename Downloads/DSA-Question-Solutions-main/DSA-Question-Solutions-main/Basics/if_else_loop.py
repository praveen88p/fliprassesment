Link = "https://www.geeksforgeeks.org/problems/java-if-else-decision-making0924/0?category%255B%255D=Java&difficulty%255B%255D=-2&page=1&query=category%255B%255DJavadifficulty%255B%255D-2page1category%255B%255DJava"

class Solution:
    def compareNM(self, n : int, m : int) -> str:
        if n<m :
            return "lesser"
        elif n==m:
            return "equal"
        else:
            return "greater"