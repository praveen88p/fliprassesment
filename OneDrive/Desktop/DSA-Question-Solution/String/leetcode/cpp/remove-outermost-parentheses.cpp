//Que - Remove-Outermost-Parentheses 
//Link - https://leetcode.com/problems/remove-outermost-parentheses/

class Solution {
public:
    string removeOuterParentheses(string s) {
        int cnt =0;
        string ans = "";
        bool flag = true;

        for(int i=0;i<s.size();i++){

            if(s[i]=='(')
            {
                cnt++;
            }
            else if(s[i]==')') cnt--;

            if(cnt==1 && flag==true){
                flag =false;
                continue;
            }
            if(cnt==0 && flag ==false){
                flag = true;
                continue;
            }
            ans+=s[i];
        }
        return ans;

    }
};
