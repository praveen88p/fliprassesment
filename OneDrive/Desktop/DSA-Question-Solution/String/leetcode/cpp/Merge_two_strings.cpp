Given two strings S1 and S2 as input, the task is to merge them alternatively i.e.
the first character of S1 then the first character of S2 and so on till the strings end.
NOTE: Add the whole string if other string is empty.

string merge (string S1, string S2)
{
    // your code here
    string ans = "";
    int i = 0;
    int j = 0;
        while(i<S1.length() && j<S2.length()){
            ans+=S1[i];
            ans+=S2[j];
            i++;
            j++;
        }
        while(i<S1.length()){
            ans+=S1[i];
            i++;
        }
         while(j<S2.length()){
            ans+=S2[j];
            j++;
        }
    return ans;
}
