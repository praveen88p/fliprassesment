Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.


  int balancedStringSplit(string s) {
      int n = s.size();
      int Rch = 0, Lch = 0;
      int count = 0;
      for(int i = 0; i<n; i++){
        if(s[i] == 'R'){
            Rch++;
        }
        else{
            Lch++;
        }

        if(Rch == Lch){
            count++;
        }
      }   
      return count;
    }

Time Complexcity = O(n) 
space Complexcity = O(1)
